import os
import sys
import yaml
from pathlib import Path

# cctv_tester 모듈 경로 추가
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

# cctv_tester.py 직접 import
import cctv_tester.cctv_tester as tester

def test_config_yaml_exists():
    """config.yaml 파일이 존재하고 필수 키를 포함하는지 테스트"""
    config_path = PROJECT_ROOT / "src" / "cctv_tester" / "config.yaml"
    assert config_path.exists(), "config.yaml 파일이 존재하지 않습니다."

    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)

    # 필수 키 검증
    for key in ["mount_point", "channel_count", "max_storage_mb",
                "log_interval_sec", "file_size_gb_per_hour",
                "block_size_kb", "file_duration_sec"]:
        assert key in cfg, f"config.yaml에 '{key}' 키가 없습니다."

def test_main_functions_exist():
    """cctv_tester 모듈의 주요 함수들이 정의되어 있는지 확인"""
    required_functions = [
        "load_config",
        "write_channel",
        "log_performance",
        "clear_old_test_files",
        "cleanup_old_files"
    ]
    for func in required_functions:
        assert hasattr(tester, func), f"{func} 함수가 cctv_tester.py에 정의되어 있지 않습니다."

def test_mount_point_writable(tmp_path):
    """mount_point 경로를 임시 디렉토리로 대체하여 쓰기 가능 여부 테스트"""
    test_file = tmp_path / "testfile.dat"
    with open(test_file, "wb") as f:
        f.write(b"test")
    assert test_file.exists(), "임시 디렉토리에 파일을 쓸 수 없습니다."
