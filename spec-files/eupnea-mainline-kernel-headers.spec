Name:       eupnea-mainline-kernel-headers
Version:    1.0.39
Release:    1%{?dist}
Summary:    Eupnea Mainline kernel headers
License:    GPLv3+
ExclusiveArch:   x86_64
Requires:    eupnea-mainline-kernel-modules

%define _build_id_links none

%description
This package contains the Eupnea Mainline kernel headers. It is only compatible with Eupnea Mainline kernels.

%prep
curl --silent -LO https://github.com/eupnea-project/linux-kernels/releases/download/latest-mainline/headers.tar.xz

%install
# Make dirs
mkdir -p %{buildroot}/usr/src

# Unpack tar
tar xfpJ headers.tar.xz -C %{buildroot}/usr/src

%files
/usr/src/linux-headers-insert_version
%ghost /lib/modules/insert_version/build

%post
#!/bin/sh

# Symlink kernel headers
# The github workflow will replace insert_version with the correct kernel version
ln -s /usr/src/linux-headers-insert_version/ /lib/modules/insert_version/build
