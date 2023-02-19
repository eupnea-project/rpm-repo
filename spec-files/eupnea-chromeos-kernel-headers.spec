Name:       eupnea-chromeos-kernel-headers
Version:    1.0.16
Release:    1%{?dist}
Summary:    Eupnea ChromeOS kernel headers
License:    GPLv3+
ExclusiveArch:   x86_64
Requires:    eupnea-chromeos-kernel-modules

%description
This package contains the Eupnea ChromeOS kernel headers. It is only compatible with Eupnea ChromeOS kernels.

%prep
#curl --silent -L https://github.com/eupnea-linux/chromeos-kernel/releases/latest/download/headers.tar.xz  -o headers.tar.xz
curl --silent -L https://github.com/eupnea-linux/chromeos-kernel/releases/download/dev-build/headers.tar.xz  -o headers.tar.xz

%install
# Make dirs
mkdir -p %{buildroot}/usr/src

# Unpack tar
tar xfpJ headers.tar.xz -C %{buildroot}/usr/src

%files
/usr/src/linux-headers-insert_version

%post
#!/bin/sh

# Symlink kernel headers
# The github workflow will replace insert_version with the correct kernel version
ln -s /usr/src/linux-headers-insert_version/ /lib/modules/insert_version/build
