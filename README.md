# ablestack-vm-perftest-tools

`ablestack-vm-perftest-tools` 는 **가상머신 내부에서 다양한 방식으로 성능을 측정**할 수 있도록 개발된 도구 모음입니다.
첫 번째 모듈로 **CCTV 시뮬레이터(`cctv_tester`)** 를 포함하고 있습니다.

---

## ✨ 주요 기능

* ✅ **RHEL / Ubuntu** 모두 지원
* ✅ GitHub clone 후 스크립트로 설치하거나 **RPM / DEB 패키지**로 설치 가능
* ✅ CCTV 카메라와 유사한 패턴의 데이터(2.6GB/시간, 512KB 블록)를 지속적으로 저장하며 디스크 성능 측정
* ✅ `config.yaml` 로 동작을 쉽게 설정
* ✅ 디스크 가득 창을 감지하고 오래된 파일을 자동으로 삭제
* ✅ 실행 중 주기적인 성능 로그(`logs/perf.log`)

---

## 📦 설치 방법

### 1. GitHub clone 후 설치

```bash
git clone https://github.com/<YOUR_ORG>/ablestack-vm-perftest-tools.git
cd ablestack-vm-perftest-tools/scripts
chmod +x install.sh
sudo ./install.sh
```

### 2. 패키지 설치 (RPM / DEB)

패키지링 디렉토리(`packaging/`)의 스크립트를 통해 RPM 또는 DEB를 빌드 후 설치할 수 있습니다.

```bash
# RPM (RHEL 계역)
sudo rpm -ivh ablestack-vm-perftest-tools-<version>.rpm

# DEB (Ubuntu 계역)
sudo dpkg -i ablestack-vm-perftest-tools-<version>.deb
```

---

## 🚀 실행 방법

설치 후 아래 명령어로 실행합니다:

```bash
cctv_tester
```

### 기본 설정

`src/cctv_tester/config.yaml` 에서 아래 항목을 조정할 수 있습니다:

| 항목                        | 기본값             | 설명              |
| ------------------------- | --------------- | --------------- |
| mount\_point              | `/mnt/testdisk` | 데이터 저장 경로       |
| channel\_count            | 4               | 동시 실행 채널 수      |
| max\_storage\_mb          | 20000           | 최대 저장 용량(MB)    |
| log\_interval\_sec        | 10              | 성능 로그 출력 주기(초)  |
| file\_size\_gb\_per\_hour | 2.6             | 1시간당 데이터량(GB)   |
| block\_size\_kb           | 512             | 블록 크기(KB)       |
| file\_duration\_sec       | 3600            | 한 파일에 저장할 시간(초) |

---

## 📖 문서

* [사용자 가이드](docs/user-guide.md)
* [개발자 가이드](docs/developer-guide.md)

---

## 🤝 기여

1. 이슈를 등록하거나 PR을 보내주세요.
2. `tests/` 디렉토리의 테스트를 통과하는지 확인해 주세요.
3. 코드 스타일과 문서를 유지해 주세요.

---

## 📜 라이선스

본 프로젝트는 [Apache License 2.0](LICENSE) 하에 배포됩니다.
