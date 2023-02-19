Name:       eupnea-chromeos-kernel
Version:    1.0.15
Release:    1%{?dist}
Summary:    Eupnea ChromeOS kernel
License:    GPLv3+
ExclusiveArch:   x86_64
# dnf is protecting currently running kernels and will therefore refuse to uninstall the conflicting package
# A systemd service was implemented instead which will delete the non-booted kernel on the next reboot
# Conflicts:  eupnea-mainline-kernel
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
mkdir -p %{buildroot}/usr/lib/systemd/system/eupnea-kernel-autoremove.service

# Copy kernel to tmp location
cp bzImage %{buildroot}/tmp/eupnea-kernel-update/bzImage

%files
/tmp/eupnea-kernel-update/bzImage

%post
#!/bin/sh

# Flash the kernel
/usr/lib/eupnea/install-kernel /tmp/eupnea-kernel-update/bzImage

# Install systemd service for kernel cleanup on next reboot
cp eupnea-kernel-autoremove.service %{buildroot}/usr/lib/systemd/system/eupnea-kernel-autoremove.service