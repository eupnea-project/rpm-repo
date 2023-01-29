Name:       eupnea-mainline-kernel
Version:    1.0.-1
Release:    1%{?dist}
Summary:    Eupnea Mainline kernel
License:    GPLv3+
ExclusiveArch:   x86_64
Conflicts:  eupnea-chromeos-kernel

%description
WARNING: This package will overwrite the first partition of your current drive!
Only use it on Chromebooks running Eupnea systems!
This package contains the Eupnea Mainline kernel. It is only compatible with x86_64 Chromebooks.

%prep
#curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/latest/download/bzImage -o bzImage
#curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/latest/download/modules.tar.xz -o modules.tar.xz
#curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/latest/download/headers.tar.xz  -o headers.tar.xz

curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/download/dev-build/bzImage -o bzImage
curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/download/dev-build/modules.tar.xz -o modules.tar.xz
curl --silent -L https://github.com/eupnea-linux/mainline-kernel/releases/download/dev-build/headers.tar.xz  -o headers.tar.xz

%install
# Make dirs
mkdir -p %{buildroot}/lib/modules
mkdir -p %{buildroot}/usr/src
mkdir -p %{buildroot}/tmp/eupnea-kernel-update

# Unpack tars
tar xfpJ modules.tar.xz -C %{buildroot}/lib/modules
tar xfpJ headers.tar.xz -C %{buildroot}/usr/src

# Read kernel version
%global kernel_version %(echo "$(file -bL ../bzImage | grep -o 'version [^ ]*' | cut -d ' ' -f 2)")

# Copy kernel to tmp location
cp bzImage %{buildroot}/tmp/eupnea-kernel-update/bzImage

# Symlink kernel headers
ln -s %{buildroot}/usr/src/linux-headers-%{kernel_version}/ %{buildroot}/lib/modules/%{kernel_version}/build

%files
/usr/src/linux-headers-%{kernel_version}/
/lib/modules/%{kernel_version}/

%post
#!/bin/sh

# Flash the kernel
/usr/lib/eupnea/install-kernel /tmp/eupnea-kernel-update/bzImage
