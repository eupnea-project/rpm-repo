Name:       eupnea-mainline-kernel
Version:    1.0.37
Release:    1%{?dist}
Summary:    Eupnea Mainline kernel
License:    GPLv3+
ExclusiveArch:   x86_64
# dnf is protecting currently running kernels and will therefore refuse to uninstall the conflicting package
# A systemd service was implemented instead which will delete the non-booted kernel on the next reboot
# Conflicts:  eupnea-chromeos-kernel
Requires:    eupnea-mainline-kernel-modules eupnea-mainline-kernel-headers eupnea-utils >= 1.1.70

%define _build_id_links none

%description
WARNING: This package will overwrite the first partition of your current drive!
Only use it on Chromebooks running Eupnea systems!
This package contains the Eupnea Mainline kernel. It is only compatible with x86_64 Chromebooks.

%prep
curl --silent -LO https://github.com/eupnea-project/linux-kernels/releases/latest/download/mainline-bzImage
git clone --depth=1 --branch=main https://github.com/eupnea-project/rpm-repo.git

%install
# Make dirs
mkdir -p %{buildroot}/boot
mkdir -p %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/lib/eupnea

# Copy kernel to /boot
cp mainline-bzImage %{buildroot}/boot/vmlinuz-eupnea-mainline

# Add kernel autoremove script
cp rpm-repo/configs/kernel-autoremove/autoremove-kernels.sh %{buildroot}/usr/lib/eupnea/autoremove-kernels.sh

# Add kernel autoremove systemd service
cp rpm-repo/configs/kernel-autoremove/kernel-autoremove.service %{buildroot}/usr/lib/systemd/system/kernel-autoremove.service

%files
/boot/vmlinuz-eupnea-mainline
/usr/lib/eupnea/autoremove-kernels.sh
/usr/lib/systemd/system/kernel-autoremove.service

%post
#!/bin/sh

# Flash the kernel
/usr/lib/eupnea/install-kernel --ignore-reboot --kernel-path /boot/vmlinuz-eupnea-mainline

# Enable kernel autoremove service
systemctl enable kernel-autoremove.service