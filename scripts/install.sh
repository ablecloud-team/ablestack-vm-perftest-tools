#!/bin/bash
set -e

INSTALL_DIR="/opt/ablestack-vm-perftest-tools"
BIN_LINK="/usr/local/bin/cctv_tester"

echo "[INFO] Installing ablestack-vm-perftest-tools..."

# --- 1. 패키지 관리자 확인 및 python3 설치 ---
install_python_and_pip() {
    if command -v dnf >/dev/null 2>&1; then
        echo "[INFO] Detected RHEL/Fedora (dnf)"
        sudo dnf install -y python3 python3-pip
    elif command -v yum >/dev/null 2>&1; then
        echo "[INFO] Detected RHEL/CentOS (yum)"
        sudo yum install -y python3 python3-pip
    elif command -v apt >/dev/null 2>&1; then
        echo "[INFO] Detected Ubuntu/Debian (apt)"
        sudo apt update
        sudo apt install -y python3 python3-pip
    else
        echo "[ERROR] Unsupported package manager. Please install Python3 and pip manually."
        exit 1
    fi
}

# --- 2. Python3 / pip 설치 확인 ---
if ! command -v python3 >/dev/null 2>&1; then
    echo "[INFO] python3 not found. Installing..."
    install_python_and_pip
else
    echo "[INFO] python3 found: $(python3 --version)"
fi

if ! command -v pip3 >/dev/null 2>&1; then
    echo "[INFO] pip3 not found. Installing..."
    install_python_and_pip
else
    echo "[INFO] pip3 found: $(pip3 --version)"
fi

# --- 3. PyYAML 설치 ---
echo "[INFO] Installing PyYAML..."
pip3 install pyyaml --break-system-packages || pip3 install pyyaml || true

# --- 4. 소스 설치 ---
echo "[INFO] Installing files to $INSTALL_DIR"
sudo mkdir -p $INSTALL_DIR
sudo cp -r ../src/cctv_tester $INSTALL_DIR/
sudo chmod +x $INSTALL_DIR/cctv_tester/cctv_tester.py

# --- 5. 심볼릭 링크 생성 ---
echo "[INFO] Creating symlink: $BIN_LINK"
sudo ln -sf $INSTALL_DIR/cctv_tester/cctv_tester.py $BIN_LINK

echo "[INFO] Installation complete."
echo "[INFO] Run with: cctv_tester"

# 권한 조정
sudo chmod -R a+rX $INSTALL_DIR
