Name:       eupnea-utils
Version:    1.1.54
Release:    1%{?dist}
Summary:    Eupnea utilities
License:    GPLv3+
ExclusiveArch:   x86_64
Requires:    vboot-utils parted rsync git strace alsa-utils

%description
This package contains a set of tools to interact with EupneaOS/Depthboot systems.
Not recommended for use on non-Chromebook devices.

%prep
git clone --depth=1 https://github.com/eupnea-linux/eupnea-utils.git
git clone --depth=1 https://github.com/eupnea-linux/audio-scripts.git

%build

%install
# Make dirs
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/eupnea/
mkdir -p %{buildroot}/%{_sysconfdir}/eupnea
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system/

# Copy scripts to bin
install -m 755 eupnea-utils/user-scripts/* %{buildroot}/%{_bindir}/
install -m 755 audio-scripts/setup-audio %{buildroot}/%{_bindir}/

# Copy scripts to lib
cp eupnea-utils/system-scripts/* %{buildroot}/usr/lib/eupnea/
cp eupnea-utils/functions.py %{buildroot}/usr/lib/eupnea/

# Copy configs
cp -r eupnea-utils/configs/* %{buildroot}/%{_sysconfdir}/eupnea/
cp -r audio-scripts/configs/* %{buildroot}/%{_sysconfdir}/eupnea/

# Copy systemd units
cp eupnea-utils/configs/systemd-services/eupnea-postinstall.service %{buildroot}/%{_sysconfdir}/systemd/system/
cp eupnea-utils/configs/systemd-services/eupnea-update.service %{buildroot}/%{_sysconfdir}/systemd/system/

%files
%{_bindir}/collect-logs
%{_bindir}/install-to-internal
%{_bindir}/modify-cmdline
%{_bindir}/setup-audio

/usr/lib/eupnea/

%{_sysconfdir}/eupnea/
%{_sysconfdir}/systemd/system/eupnea-postinstall.service
%{_sysconfdir}/systemd/system/eupnea-update.service
