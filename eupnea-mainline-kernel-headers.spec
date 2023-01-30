Name:       eupnea-mainline-kernel-headers
Version:    1.0.0
Release:    1%{?dist}
Summary:    Eupnea Mainline kernel headers
License:    GPLv3+
ExclusiveArch:   x86_64

%description
This package contains the Eupnea Mainline kernel headers. It is only compatible with Eupnea Mainline kernels.

%prep
#curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/latest/download/headers.tar.xz  -o headers.tar.xz
curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/download/dev-build/headers.tar.xz  -o headers.tar.xz

%install
# Make dirs
mkdir -p %{buildroot}/usr/src

# Unpack tar
tar xfpJ headers.tar.xz -C %{buildroot}/usr/src

%files
/*

%post
#!/bin/sh

# Symlink kernel headers
# The github workflow will replace insert_version with the correct kernel version
ln -s /usr/src/linux-headers-insert_version/ /lib/modules/insert_version/build
