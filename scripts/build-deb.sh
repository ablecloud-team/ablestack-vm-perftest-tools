#!/bin/bash
set -e

PKG_NAME="ablestack-vm-perftest-tools"
PKG_VERSION="0.1.0"
WORKDIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "[INFO] Starting DEB build for $PKG_NAME $PKG_VERSION"

# 1. tarball 생성 (소스와 문서 포함)
echo "[INFO] Creating source tarball..."
cd "$WORKDIR"
TARBALL="${PKG_NAME}_${PKG_VERSION}.orig.tar.gz"
tar czf "/tmp/$TARBALL" \
    README.md LICENSE CHANGELOG.md src

# 2. 빌드용 디렉토리 준비
BUILD_DIR="/tmp/${PKG_NAME}-${PKG_VERSION}"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"
cp -r src "$BUILD_DIR/"
cp README.md LICENSE CHANGELOG.md "$BUILD_DIR/"

# 3. debian 디렉토리 복사
mkdir -p "$BUILD_DIR/debian"
cp -r packaging/debian/* "$BUILD_DIR/debian/"

# 4. 빌드 수행
cd "$BUILD_DIR"
echo "[INFO] Running dpkg-buildpackage..."
dpkg-buildpackage -us -uc

echo "[INFO] DEB build completed."
echo "[INFO] Output DEB files are in: /tmp"
