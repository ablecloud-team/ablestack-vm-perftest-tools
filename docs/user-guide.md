# User Guide

## 📌 개요

`ablestack-vm-perftest-tools` 프로젝트의 첫 번째 모듈인 **cctv\_tester** 사용 가이드입니다. 이 도구는 가상머신 내부에서 CCTV 카메라의 데이터 전송 패턴을 시뮬레이션하며 디스크 성능을 테스트합니다.

---

## ⚙️ 요구 사항

* Python 3.8 이상
* PyYAML 라이브러리
* RHEL 계열 또는 Ubuntu 계열 리눅스

설치 방법은 [README.md](../README.md)를 참고하세요.

---

## 🚀 실행 방법

설치 후 아래 명령으로 실행합니다.

```bash
cctv_tester
```

실행 시 기본 설정 파일은 다음 경로를 사용합니다:

```
src/cctv_tester/config.yaml
```

---

## 📝 설정 파일 (config.yaml)

아래는 주요 설정 항목입니다.

| 키                       | 설명               | 기본값             |
| ----------------------- | ---------------- | --------------- |
| `mount_point`           | 데이터가 저장될 디렉토리 경로 | `/mnt/testdisk` |
| `channel_count`         | 동시 실행 채널 수       | 4               |
| `max_storage_mb`        | 디스크 최대 사용 용량(MB) | 20000           |
| `log_interval_sec`      | 성능 로그 출력 주기(초)   | 10              |
| `file_size_gb_per_hour` | 1시간당 데이터량(GB)    | 2.6             |
| `block_size_kb`         | 한 블록의 크기(KB)     | 512             |
| `file_duration_sec`     | 한 파일에 저장할 시간(초)  | 3600            |

실제 테스트 시에는 `mount_point` 디렉토리가 존재하고 쓰기 가능해야 합니다. 실행 전 디렉토리를 미리 생성해 두거나, 설치 스크립트가 생성한 경로를 사용하세요.

---

## 📈 로그 확인

프로그램 실행 중 `logs/perf.log` 에 주기적인 성능 데이터가 기록됩니다.

```
2025-07-25T13:20:00 | Write Speed: 65.20 MB/s | Total Written: 10240.50 MB
```

---

## 🧹 공간 관리

디스크 사용량이 `max_storage_mb`를 초과하면 오래된 파일부터 자동으로 삭제하여 테스트를 계속할 수 있도록 설계되어 있습니다.

---

## 🛠️ 문제 해결

* **`No space left on device` 에러 발생**: `max_storage_mb` 값을 늘리거나, 충분한 디스크 공간이 있는지 확인하세요.
* **설정 변경이 반영되지 않음**: 실행 중에는 설정 파일이 다시 로드되지 않습니다. 프로그램을 중단 후 다시 실행하세요.

---

## 📬 문의 및 기여

* GitHub 이슈를 통해 문의 및 개선 요청을 남겨주세요.
* PR 제출 전 `pytest` 테스트를 통과하는지 확인해 주세요.

**이 문서는 `docs/user-guide.md` 입니다.**
