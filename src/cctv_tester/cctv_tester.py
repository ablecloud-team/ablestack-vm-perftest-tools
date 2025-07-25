import os, time, threading, yaml
from pathlib import Path
from datetime import datetime

# 기본 설정
MOUNT_POINT = "/mnt/testdisk"
CHANNEL_COUNT = 4
MAX_STORAGE_MB = 20000
LOG_INTERVAL = 10
FILE_SIZE_GB_PER_HOUR = 2.6
BLOCK_SIZE_KB = 512
FILE_DURATION_SEC = 3600

# 내부 상태
write_bytes_total = 0
write_bytes_lock = threading.Lock()
stop_flag = False
cleanup_lock = threading.Lock()

def load_config():
    global MOUNT_POINT, CHANNEL_COUNT, MAX_STORAGE_MB, LOG_INTERVAL
    global FILE_SIZE_GB_PER_HOUR, BLOCK_SIZE_KB, FILE_DURATION_SEC
    cfg_path = Path("config.yaml")
    if not cfg_path.exists():
        print("[WARN] config.yaml not found. Using default settings.")
        return
    with open(cfg_path, "r") as f:
        cfg = yaml.safe_load(f)
    MOUNT_POINT = cfg.get("mount_point", MOUNT_POINT)
    CHANNEL_COUNT = cfg.get("channel_count", CHANNEL_COUNT)
    MAX_STORAGE_MB = cfg.get("max_storage_mb", MAX_STORAGE_MB)
    LOG_INTERVAL = cfg.get("log_interval_sec", LOG_INTERVAL)
    FILE_SIZE_GB_PER_HOUR = cfg.get("file_size_gb_per_hour", FILE_SIZE_GB_PER_HOUR)
    BLOCK_SIZE_KB = cfg.get("block_size_kb", BLOCK_SIZE_KB)
    FILE_DURATION_SEC = cfg.get("file_duration_sec", FILE_DURATION_SEC)
    print("[CONFIG] Loaded configuration:")
    for k, v in cfg.items():
        print(f"  {k}: {v}")

def get_storage_usage_mb(path):
    stat = os.statvfs(path)
    used = (stat.f_blocks - stat.f_bfree) * stat.f_frsize
    return used / (1024 * 1024)

def cleanup_old_files(path):
    with cleanup_lock:
        file_list = []
        for f in Path(path).glob("channel_*_*.dat"):
            try:
                mtime = f.stat().st_mtime
                file_list.append((mtime, f))
            except FileNotFoundError:
                continue
        files = [f for _, f in sorted(file_list, key=lambda x: x[0])]
        used = get_storage_usage_mb(path)
        while used > MAX_STORAGE_MB and files:
            oldest = files.pop(0)
            try:
                os.remove(oldest)
                print(f"[CLEANUP] Removed {oldest}")
            except FileNotFoundError:
                pass
            except Exception as e:
                print(f"[CLEANUP ERROR] {e}")
            used = get_storage_usage_mb(path)

def write_channel(channel_id, file_size_bytes, block_size_bytes, blocks_per_file, sleep_per_block):
    global write_bytes_total
    channel_dir = Path(MOUNT_POINT)
    channel_dir.mkdir(parents=True, exist_ok=True)
    file_index = 0
    block = os.urandom(block_size_bytes)
    while not stop_flag:
        filename = channel_dir / f"channel_{channel_id}_{file_index:06d}.dat"
        with open(filename, "wb") as f:
            for _ in range(blocks_per_file):
                if get_storage_usage_mb(MOUNT_POINT) > MAX_STORAGE_MB:
                    cleanup_old_files(MOUNT_POINT)
                try:
                    start_t = time.time()
                    f.write(block)
                    with write_bytes_lock:
                        write_bytes_total += len(block)
                except OSError as e:
                    if e.errno == 28:  # No space left
                        print(f"[WARN] Disk full on channel {channel_id}, cleaning up...")
                        cleanup_old_files(MOUNT_POINT)
                        time.sleep(1)
                        continue
                    else:
                        raise
                elapsed = time.time() - start_t
                to_sleep = sleep_per_block - elapsed
                if to_sleep > 0:
                    time.sleep(to_sleep)
                if stop_flag:
                    break
        file_index += 1

def log_performance():
    global write_bytes_total
    prev_bytes = 0
    while not stop_flag:
        time.sleep(LOG_INTERVAL)
        with write_bytes_lock:
            current_bytes = write_bytes_total
        delta = current_bytes - prev_bytes
        prev_bytes = current_bytes
        mb_per_sec = (delta / (1024 * 1024)) / LOG_INTERVAL
        log_line = f"{datetime.now().isoformat()} | Write Speed: {mb_per_sec:.2f} MB/s | Total Written: {current_bytes/1024/1024:.2f} MB"
        print(log_line)
        with open("logs/perf.log", "a") as lf:
            lf.write(log_line + "\n")

def clear_old_test_files():
    test_dir = Path(MOUNT_POINT)
    if not test_dir.exists():
        return
    removed_count = 0
    for f in test_dir.glob("channel_*_*.dat"):
        try:
            f.unlink()
            removed_count += 1
        except Exception:
            continue
    if removed_count > 0:
        print(f"[INIT] Removed {removed_count} old test files in {MOUNT_POINT}")

def main():
    load_config()

    # 파일 크기 계산 (시간 단위)
    file_size_bytes = int(FILE_SIZE_GB_PER_HOUR * (FILE_DURATION_SEC / 3600) * 1024 * 1024 * 1024)
    block_size_bytes = BLOCK_SIZE_KB * 1024
    blocks_per_file = file_size_bytes // block_size_bytes
    sleep_per_block = FILE_DURATION_SEC / blocks_per_file

    print(f"[INFO] Each file: {FILE_DURATION_SEC}s, {file_size_bytes/1024/1024:.2f} MB, {blocks_per_file} blocks, interval {sleep_per_block:.3f}s")

    os.makedirs("logs", exist_ok=True)
    clear_old_test_files()

    threads = []
    for cid in range(CHANNEL_COUNT):
        t = threading.Thread(
            target=write_channel,
            args=(cid, file_size_bytes, block_size_bytes, blocks_per_file, sleep_per_block),
            daemon=True
        )
        threads.append(t)
        t.start()

    log_thread = threading.Thread(target=log_performance, daemon=True)
    log_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        global stop_flag
        stop_flag = True
        print("Stopping...")

if __name__ == "__main__":
    main()
