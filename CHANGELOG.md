# Changelog

## \[0.1.0] - 2025-07-26

### Added

* Initial release of **ablestack-vm-perftest-tools** project.
* Added `cctv_tester` module for simulating CCTV-like disk write patterns.
* Provided cross-platform install script (`install.sh`) for RHEL and Ubuntu.
* Added packaging scripts and metadata:

  * RPM build support (`build-rpm.sh`, `.spec` file)
  * DEB build support (`build-deb.sh`, `debian/control`, etc.)
* Added project documentation:

  * `README.md` with usage instructions
  * `docs/user-guide.md` with detailed usage
  * `docs/developer-guide.md` for contributors

### Notes

* This is the first public version of the project.
* Future updates will add more VM performance testing modules and improved logging.

---

## \[Planned]

* Add network performance tester module.
* Extend configuration options.
* CI/CD integration for automated package builds.
