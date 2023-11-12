Name:       eupnea-mainline-kernel-modules
Version:    1.0.35
Release:    1%{?dist}
Summary:    Eupnea Mainline kernel
License:    GPLv3+
ExclusiveArch:   x86_64

%define _build_id_links none

%description
This package contains the Eupnea Mainline kernel modules. It is only compatible with Eupnea Mainline kernels.

%prep
curl --silent -LO https://github.com/eupnea-project/mainline-kernel/releases/latest/download/mainline-modules.tar.xz

%install
# Make dirs
mkdir -p %{buildroot}/lib/modules

# Unpack tars
tar xfpJ mainline-modules.tar.xz -C %{buildroot}/lib/modules

%files
/lib/modules/insert_version
