# Makefile for ablestack-vm-perftest-tools
# ----------------------------------------

.PHONY: all install rpm deb uninstall clean

# 기본 안내
all:
	@echo "Available targets:"
	@echo "  make install    - Install tools to system"
	@echo "  make rpm        - Build RPM package"
	@echo "  make deb        - Build DEB package"
	@echo "  make uninstall  - Uninstall tools from system"
	@echo "  make clean      - Clean temporary build artifacts"

# 설치
install:
	cd scripts && chmod +x install.sh && ./install.sh

# RPM 빌드
rpm:
	cd scripts && chmod +x build-rpm.sh && ./build-rpm.sh

# DEB 빌드
deb:
	cd scripts && chmod +x build-deb.sh && ./build-deb.sh

# 제거
uninstall:
	cd scripts && chmod +x uninstall.sh && ./uninstall.sh

# 빌드 산출물 제거
clean:
	rm -rf /tmp/ablestack-vm-perftest-tools-* \
	       /tmp/ablestack-vm-perftest-tools_*.orig.tar.gz \
	       ~/rpmbuild/BUILD/ablestack-vm-perftest-tools-* || true
	@echo "Cleaned temporary build artifacts."
