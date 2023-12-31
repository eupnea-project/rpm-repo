Name:       eupnea-chromeos-kernel-modules
Version:    1.0.37
Release:    1%{?dist}
Summary:    Eupnea ChromeOS kernel
License:    GPLv3+
ExclusiveArch:   x86_64

%define _build_id_links none

%description
This package contains the Eupnea ChromeOS kernel modules. It is only compatible with Eupnea ChromeOS kernels.

%prep
curl --silent -LO https://github.com/eupnea-project/linux-kernels/releases/download/latest-chromeos/modules.tar.xz

%install
# Make dirs
mkdir -p %{buildroot}/lib/modules

# Unpack tars
tar xfpJ modules.tar.xz -C %{buildroot}/lib/modules

%files
/lib/modules/insert_version
