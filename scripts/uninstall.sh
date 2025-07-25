#!/bin/bash
set -e

INSTALL_DIR="/opt/ablestack-vm-perftest-tools"
BIN_LINK="/usr/local/bin/cctv_tester"

echo "[INFO] Uninstalling ablestack-vm-perftest-tools..."

read -p "Really uninstall? [y/N] " ans
if [[ "$ans" != "y" && "$ans" != "Y" ]]; then
    echo "Cancelled."
    exit 0
fi

# 심볼릭 링크 제거
if [ -L "$BIN_LINK" ] || [ -f "$BIN_LINK" ]; then
    echo "[INFO] Removing symlink: $BIN_LINK"
    sudo rm -f "$BIN_LINK"
else
    echo "[INFO] Symlink not found: $BIN_LINK"
fi

# 설치 디렉토리 제거
if [ -d "$INSTALL_DIR" ]; then
    echo "[INFO] Removing install directory: $INSTALL_DIR"
    sudo rm -rf "$INSTALL_DIR"
else
    echo "[INFO] Install directory not found: $INSTALL_DIR"
fi

echo "[INFO] Uninstall complete."
