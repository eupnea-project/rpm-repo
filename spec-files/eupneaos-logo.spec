Name:       eupneaos-logo
Version:    1.0.3
Release:    1%{?dist}
Summary:    Alpine busybox-static + eupneaos logo boot splash
License:    GPLv2
ExclusiveArch:   x86_64

%description
Prints a eupneaos logo on boot using fbsplash from Alpine Linux's busybox-static package

%prep
# Determine the latest alpine static busybox package name
package_name=$(curl -L https://dl-cdn.alpinelinux.org/alpine/latest-stable/main/x86_64/ | grep busybox-static-  | awk -F'>' '{print $2}' | awk -F'<' '{print $1}')
# download the latest alpine busybox package
curl -LO https://dl-cdn.alpinelinux.org/alpine/latest-stable/main/x86_64/$package_name

%install
# Make dirs
mkdir -p busybox-extracted
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/eupnea
mkdir -p %{buildroot}/usr/lib/systemd/system

# Extract the alpine package
tar xfpz busybox-static-*.apk --warning=no-unknown-keyword -C busybox-extracted
# copy busybox binary into the package
install -Dm755 busybox-extracted/bin/busybox.static %{buildroot}/%{_bindir}/busybox-alpine.static

# copy eupneaos logo into the package
cp eupneaos-logo/eupneaos.ppm %{buildroot}/%{_datadir}/eupnea/eupnea_boot_logo.ppm

# Copy config for centering the logo
cp eupneaos-logo/center-splash.conf %{buildroot}/%{_datadir}/eupnea/center-splash.conf

# add systemd service
cp eupneaos-logo/eupnea-boot-splash.service %{buildroot}/usr/lib/systemd/system/eupnea-boot-splash.service

%files
%{_bindir}/busybox-alpine.static

/usr/lib/systemd/system/eupnea-boot-splash.service

%{_datadir}/eupnea/eupnea_boot_logo.ppm
%{_datadir}/eupnea/center-splash.conf

%post
#!/bin/sh

# Enable eupneaos boot splash systemd service
systemctl enable eupnea-boot-splash.service
