# Developer Guide

이 문서는 `ablestack-vm-perftest-tools` 프로젝트에 기여하거나 내부를 이해하려는 개발자를 위한 가이드입니다.

---

## 📌 프로젝트 구조

```
ablestack-vm-perftest-tools/
├── README.md                # 사용자 가이드
├── LICENSE                  # 라이선스
├── CHANGELOG.md             # 변경 내역
├── docs/                    # 문서
│   ├── user-guide.md
│   ├── developer-guide.md
│   └── examples/
│       └── sample-config.yaml
├── scripts/                 # 설치 및 빌드 스크립트
│   ├── install.sh
│   ├── build-rpm.sh
│   ├── build-deb.sh
│   └── uninstall.sh
├── src/                     # 소스 코드
│   ├── cctv_tester/
│   │   ├── cctv_tester.py
│   │   ├── config.yaml
│   │   └── __init__.py
│   └── common/
│       ├── config_loader.py
│       └── __init__.py
├── packaging/               # 패키징 파일
│   ├── rpm/
│   │   └── ablestack-vm-perftest-tools.spec
│   └── debian/
│       ├── control
│       ├── rules
│       ├── changelog
│       └── compat
└── tests/                   # 테스트 코드
    └── test_cctv_tester.py
```

---

## ⚙️ 개발 환경 준비

1. **Python 3.8 이상** 설치
2. PyYAML 설치

```bash
pip3 install pyyaml
```

3. `pytest` 설치 (테스트용)

```bash
pip3 install pytest
```

---

## 🚀 실행 및 개발

* `src/cctv_tester/cctv_tester.py` 가 메인 실행 파일입니다.
* 설정은 `src/cctv_tester/config.yaml` 를 수정하여 적용합니다.

개발 시 아래 명령어로 직접 실행할 수 있습니다.

```bash
python3 src/cctv_tester/cctv_tester.py
```

---

## 📦 패키징

### RPM 빌드 (RHEL 계열)

```bash
cd scripts
chmod +x build-rpm.sh
./build-rpm.sh
```

RPM 빌드 결과는 `~/rpmbuild/RPMS/noarch/` 등에 생성됩니다.

### DEB 빌드 (Ubuntu 계열)

```bash
cd scripts
chmod +x build-deb.sh
./build-deb.sh
```

---

## ✅ 테스트 실행

```bash
pytest tests/
```

`test_cctv_tester.py` 파일이 기본 테스트를 포함합니다. 필요에 따라 테스트를 추가하세요.

---

## 🔧 코드 가이드라인

* 공통 기능은 `src/common/` 디렉토리에 구현하여 재사용성을 높입니다.
* 새 모듈 추가 시 `src/` 하위에 디렉토리를 생성하고, `__init__.py` 를 추가해 패키지로 관리합니다.
* 문서(`docs/`)를 항상 최신으로 유지합니다.

---

## 🤝 기여 방법

1. 새로운 브랜치를 생성하고 변경사항을 커밋합니다.
2. PR(Pull Request)을 통해 리뷰 요청을 보냅니다.
3. PR 전 테스트가 모두 통과하는지 확인하세요.

---

## 📜 라이선스

본 프로젝트는 [Apache License 2.0](../LICENSE) 을 따릅니다.

**이 문서는 `docs/developer-guide.md` 입니다.**
