#!/bin/bash
set -e

# --- 설정 ---
PKG_NAME="ablestack-vm-perftest-tools"
PKG_VERSION="0.1.0"
WORKDIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "[INFO] Starting RPM build for $PKG_NAME $PKG_VERSION"

# --- tarball 생성 ---
echo "[INFO] Creating source tarball..."
cd "$WORKDIR"
tar czf /tmp/${PKG_NAME}-${PKG_VERSION}.tar.gz \
    README.md LICENSE CHANGELOG.md src

# --- rpmbuild 디렉토리 준비 ---
RPMBUILD_DIR="${HOME}/rpmbuild"
mkdir -p $RPMBUILD_DIR/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

echo "[INFO] Copying sources and spec..."
cp /tmp/${PKG_NAME}-${PKG_VERSION}.tar.gz $RPMBUILD_DIR/SOURCES/
cp packaging/rpm/${PKG_NAME}.spec $RPMBUILD_DIR/SPECS/

# --- 빌드 ---
echo "[INFO] Running rpmbuild..."
rpmbuild -ba $RPMBUILD_DIR/SPECS/${PKG_NAME}.spec

echo "[INFO] RPM build completed."
echo "[INFO] Output RPMs are in: $RPMBUILD_DIR/RPMS/"
