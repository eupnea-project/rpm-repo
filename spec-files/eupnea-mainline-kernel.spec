Name:       eupnea-mainline-kernel
Version:    1.0.18
Release:    1%{?dist}
Summary:    Eupnea Mainline kernel
License:    GPLv3+
ExclusiveArch:   x86_64
# dnf is protecting currently running kernels and will therefore refuse to uninstall the conflicting package
# A systemd service was implemented instead which will delete the non-booted kernel on the next reboot
# Conflicts:  eupnea-chromeos-kernel
Requires:    eupnea-mainline-kernel-modules eupnea-mainline-kernel-headers eupnea-utils

%define _build_id_links none

%description
WARNING: This package will overwrite the first partition of your current drive!
Only use it on Chromebooks running Eupnea systems!
This package contains the Eupnea Mainline kernel. It is only compatible with x86_64 Chromebooks.

%prep
#curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/latest/download/bzImage -o bzImage
curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/download/dev-build/bzImage -o bzImage

%install
# Make dirs
mkdir -p %{buildroot}/boot
mkdir -p %{buildroot}/usr/lib/systemd/system/eupnea-kernel-autoremove.service

# Copy kernel to /boot
cp bzImage %{buildroot}/boot/vmlinuz-eupnea-mainline

%files
/boot/vmlinuz-eupnea-mainline
/usr/lib/systemd/system/eupnea-kernel-autoremove.service

%post
#!/bin/sh

# Flash the kernel
/usr/lib/eupnea/install-kernel /boot/vmlinuz-eupnea-mainline

# Install systemd service for kernel cleanup on next reboot
cp eupnea-kernel-autoremove.service %{buildroot}/usr/lib/systemd/system/eupnea-kernel-autoremove.service