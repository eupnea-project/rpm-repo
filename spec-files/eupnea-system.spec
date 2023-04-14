Name:       eupnea-system
Version:    1.0.57
Release:    1%{?dist}
Summary:    Eupnea system updater
License:    GPLv3+
ExclusiveArch:   x86_64
Requires:    eupnea-utils >= 1.1.96

%description
This package upgrades Depthboot/EupneaOS systems to the latest version.
Not recommended for use on non-Chromebook devices.

%prep
git clone --depth=1 https://github.com/eupnea-linux/system-update.git
git clone --depth=1 --branch=main https://github.com/eupnea-linux/rpm-repo.git

%build

%install
# Make dirs
mkdir -p %{buildroot}/usr/lib/eupnea-system-update/configs/

# Copy config files
cp -r system-update/configs/* %{buildroot}/usr/lib/eupnea-system-update/configs/

# Copy the update scripts and functions.py
install -Dm 755 system-update/system-update.py %{buildroot}/usr/lib/eupnea-system-update
cp system-update/functions.py %{buildroot}/usr/lib/eupnea-system-update
cp system-update/eupnea_os_updates.py %{buildroot}/usr/lib/eupnea-system-update
cp system-update/depthboot_updates.py %{buildroot}/usr/lib/eupnea-system-update

%files
/usr/lib/eupnea-system-update/

%post
#!/bin/sh

# This executes the system-update.py script in /usr/lib/eupnea-system-update after install or update
/usr/lib/eupnea-system-update/system-update.py
