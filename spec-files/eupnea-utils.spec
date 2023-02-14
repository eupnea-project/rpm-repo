Name:       eupnea-utils
Version:    1.1.29
Release:    1%{?dist}
Summary:    Eupnea utilities
License:    GPLv3+
ExclusiveArch:   x86_64
Requires:    vboot-utils parted rsync git

%description
This package contains a set of tools to interact with EupneaOS/Depthboot systems.
Not recommended for use on non-Chromebook devices.

%prep
git clone --depth=1 https://github.com/eupnea-linux/postinstall-scripts.git
git clone --depth=1 https://github.com/eupnea-linux/audio-scripts.git

%build

%install
# Make dirs
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/eupnea/
mkdir -p %{buildroot}/%{_sysconfdir}/eupnea
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system/

# Copy scripts to bin
install -m 755 postinstall-scripts/user-scripts/* %{buildroot}/%{_bindir}/
install -m 755 audio-scripts/setup-audio %{buildroot}/%{_bindir}/

# Copy scripts to lib
cp postinstall-scripts/system-scripts/* %{buildroot}/usr/lib/eupnea/
cp postinstall-scripts/functions.py %{buildroot}/usr/lib/eupnea/

# Copy configs
cp -r postinstall-scripts/configs/* %{buildroot}/%{_sysconfdir}/eupnea/
cp -r audio-scripts/configs/* %{buildroot}/%{_sysconfdir}/eupnea/

# Copy systemd units
cp postinstall-scripts/systemd-services/eupnea-postinstall.service %{buildroot}/%{_sysconfdir}/systemd/system/

%files
%{_bindir}/collect-logs
%{_bindir}/install-to-internal
%{_bindir}/manage-kernels
%{_bindir}/modify-cmdline
%{_bindir}/setup-audio

/usr/lib/eupnea/

%{_sysconfdir}/eupnea/
%{_sysconfdir}/systemd/system/eupnea-postinstall.service
