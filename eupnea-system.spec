Name:       eupnea-system
Version:    0.0.4
Release:    1%{?dist}
Summary:    Eupnea system updater
License:    GPLv3+
ExclusiveArch:   x86_64

%description
This package upgrades Depthboot/EupneaOS systems to the latest version.
Not recommended for use on non-Chromebook devices.

%prep
git clone --depth=1 https://github.com/eupnea-linux/system-update.git
git clone --depth=1 https://github.com/eupnea-linux/rpm-repo.git

%build

%install
# Make dirs
mkdir -p %{buildroot}/tmp/eupnea-system-update/configs/

# Copy config files
cp -r system-update/configs/* %{buildroot}/tmp/eupnea-system-update/configs/

# Copy the update scripts and functions.py
install -Dm 755 system-update/system-update.py %{buildroot}/tmp/eupnea-system-update
cp system-update/functions.py %{buildroot}/tmp/eupnea-system-update
cp system-update/eupnea_os_updates.py %{buildroot}/tmp/eupnea-system-update
cp system-update/depthboot_updates.py %{buildroot}/tmp/eupnea-system-update

%files
/tmp/eupnea-system-update/*

%post
#!/bin/sh

# This executes the system-update.py script in /tmp/eupnea-system-update after install or update
/tmp/eupnea-system-update/system-update.py

%changelog