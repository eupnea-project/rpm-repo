Name:       eupnea-utils
Version:    1.1.99
Release:    1%{?dist}
Summary:    Eupnea utilities
License:    GPLv3+
ExclusiveArch:   x86_64
Requires:    vboot-utils parted rsync git strace alsa-ucm-utils

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
mkdir -p %{buildroot}/usr/lib/systemd/system-sleep/
mkdir -p %{buildroot}/%{_datadir}/eupnea
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system/

# Copy scripts to bin
install -m 755 eupnea-utils/user-scripts/* %{buildroot}/%{_bindir}/
install -m 755 audio-scripts/setup-audio %{buildroot}/%{_bindir}/

# Copy scripts to lib
cp eupnea-utils/system-scripts/* %{buildroot}/usr/lib/eupnea/
cp eupnea-utils/functions.py %{buildroot}/usr/lib/eupnea/

# Copy configs
cp -r audio-scripts/configs/* %{buildroot}/%{_datadir}/eupnea/

# Copy systemd units
cp eupnea-utils/systemd-services/* %{buildroot}/%{_sysconfdir}/systemd/system/

# Add sleep trigger
install -Dm 755 eupnea-utils/configs/fix-touchscreen-on-wakeup.sh %{buildroot}/usr/lib/systemd/system-sleep/fix-touchscreen-on-wakeup.sh

%files
%{_bindir}/collect-logs
%{_bindir}/install-to-internal
%{_bindir}/modify-cmdline
%{_bindir}/setup-audio

/usr/lib/eupnea/install-kernel
/usr/lib/eupnea/modify-packages
/usr/lib/eupnea/postinstall
/usr/lib/eupnea/functions.py
/usr/lib/eupnea/fix-touchscreen.sh
/usr/lib/eupnea/set-keymap

/usr/lib/systemd/system-sleep/fix-touchscreen-on-wakeup.sh

%{_datadir}/eupnea/
%{_sysconfdir}/systemd/system/eupnea-postinstall.service
%{_sysconfdir}/systemd/system/eupnea-update.service
%{_sysconfdir}/systemd/system/touchscreen-fix.service

%post
#!/bin/sh

# Enable touchscreen fix service
systemctl enable touchscreen-fix.service
systemd-detect-virt -r || systemctl start touchscreen-fix.service # systemd-detect-virt -r returns 1 if not in a chroot
