Name:       eupnea-chromeos-kernel
Version:    1.0.7
Release:    1%{?dist}
Summary:    Eupnea ChromeOS kernel
License:    GPLv3+
ExclusiveArch:   x86_64
Conflicts:  eupnea-mainline-kernel
Requires:    eupnea-chromeos-kernel-modules eupnea-chromeos-kernel-headers eupnea-utils

%description
WARNING: This package will overwrite the first partition of your current drive!
Only use it on Chromebooks running Eupnea systems!
This package contains the Eupnea ChromeOS kernel. It is only compatible with x86_64 Chromebooks.

%prep
#curl --silent -L https://github.com/eupnea-linux/chromeos-kernel/releases/latest/download/bzImage -o bzImage
curl --silent -L https://github.com/eupnea-linux/chromeos-kernel/releases/download/dev-build/bzImage -o bzImage

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
