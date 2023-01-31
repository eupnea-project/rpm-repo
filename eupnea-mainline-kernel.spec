Name:       eupnea-mainline-kernel
Version:    1.0.3
Release:    1%{?dist}
Summary:    Eupnea Mainline kernel
License:    GPLv3+
ExclusiveArch:   x86_64
Conflicts:  eupnea-chromeos-kernel
Requires:    eupnea-mainline-kernel-modules eupnea-mainline-kernel-headers eupnea-utils

%description
WARNING: This package will overwrite the first partition of your current drive!
Only use it on Chromebooks running Eupnea systems!
This package contains the Eupnea Mainline kernel. It is only compatible with x86_64 Chromebooks.

%prep
#curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/latest/download/bzImage -o bzImage
curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/download/dev-build/bzImage -o bzImage

%install
# Make dirs
mkdir -p %{buildroot}/tmp/eupnea-kernel-update

# Copy kernel to tmp location
cp bzImage %{buildroot}/tmp/eupnea-kernel-update/bzImage

%files
/tmp/eupnea-kernel-update/bzImage

%post
#!/bin/sh

# Flash the kernel
/usr/lib/eupnea/install-kernel /tmp/eupnea-kernel-update/bzImage
