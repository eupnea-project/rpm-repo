Name:       eupnea-chromeos-kernel
Version:    1.0.33
Release:    1%{?dist}
Summary:    Eupnea ChromeOS kernel
License:    GPLv3+
ExclusiveArch:   x86_64
# dnf is protecting currently running kernels and will therefore refuse to uninstall the conflicting package
# A systemd service was implemented instead which will delete the non-booted kernel on the next reboot
# Conflicts:  eupnea-mainline-kernel
Requires:    eupnea-chromeos-kernel-modules eupnea-chromeos-kernel-headers eupnea-utils >= 1.1.70

%define _build_id_links none

%description
WARNING: This package will overwrite the first partition of your current drive!
Only use it on Chromebooks running Eupnea systems!
This package contains the Eupnea ChromeOS kernel. It is only compatible with x86_64 Chromebooks.

%prep
curl --silent -LO https://github.com/eupnea-linux/chromeos-kernel/releases/latest/download/bzImage
git clone --depth=1 --branch=main https://github.com/eupnea-linux/rpm-repo.git

%install
# Make dirs
mkdir -p %{buildroot}/boot
mkdir -p %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/lib/eupnea

# Copy kernel to /boot
cp bzImage %{buildroot}/boot/vmlinuz-eupnea-chromeos

# Add kernel autoremove script
cp rpm-repo/configs/kernel-autoremove/autoremove-kernels.sh %{buildroot}/usr/lib/eupnea/autoremove-kernels.sh

# Add kernel autoremove systemd service
cp rpm-repo/configs/kernel-autoremove/kernel-autoremove.service %{buildroot}/usr/lib/systemd/system/kernel-autoremove.service

%files
/boot/vmlinuz-eupnea-chromeos
/usr/lib/eupnea/autoremove-kernels.sh
/usr/lib/systemd/system/kernel-autoremove.service

%post
#!/bin/sh
set -e # exit on error
# Flash the kernel
/usr/lib/eupnea/install-kernel --ignore-reboot --kernel-path /boot/vmlinuz-eupnea-chromeos

# Enable kernel autoremove service
systemctl enable kernel-autoremove.service
