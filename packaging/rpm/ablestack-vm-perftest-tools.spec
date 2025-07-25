Name:           ablestack-vm-perftest-tools
Version:        0.1.0
Release:        1%{?dist}
Summary:        VM performance test tools including CCTV tester

License:        Apache-2.0
URL:            https://github.com/your-org/ablestack-vm-perftest-tools
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3, python3-devel
Requires:       python3, python3-pyyaml

%description
A set of tools to test and monitor VM internal performance.
This package includes a CCTV tester module that simulates
CCTV-like data generation and storage patterns to test disk performance.

%prep
%autosetup

%build
# Pure Python scripts, no build steps required

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/%{name}
cp -a src/cctv_tester %{buildroot}/opt/%{name}/
mkdir -p %{buildroot}/usr/local/bin
ln -sf /opt/%{name}/cctv_tester/cctv_tester.py %{buildroot}/usr/local/bin/cctv_tester

%files
/opt/%{name}
/usr/local/bin/cctv_tester

%doc README.md LICENSE CHANGELOG.md

%changelog
* Fri Jul 26 2025 ABLECLOUD <info@ablecloud.io> - 0.1.0-1
- Initial release with cctv_tester module
