Name:       eupnea-utils
Version:    0.0.9
Release:    1%{?dist}
Summary:    Eupnea utilities
License:    GPLv3+
ExclusiveArch:   x86_64
Requires:    vboot-utils

%description
This package contains a set of tools to interact with EupneaOS/Depthboot systems.
Not recommended for use on non-Chromebook devices.

%prep
git clone --depth=1 https://github.com/eupnea-linux/postinstall-scripts.git --branch=move-to-packages
git clone --depth=1 https://github.com/eupnea-linux/audio-scripts.git

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/eupnea
install -m 755 postinstall-scripts/scripts/* %{buildroot}/%{_bindir}/
install -m 755 audio-scripts/setup-audio %{buildroot}/%{_bindir}/
cp -r postinstall-scripts/configs/* %{buildroot}/%{_sysconfdir}/eupnea/
cp -r audio-scripts/configs/* %{buildroot}/%{_sysconfdir}/eupnea/

%files
%{_bindir}/collect-logs
%{_bindir}/functions.py
%{_bindir}/install-to-internal
%{_bindir}/manage-kernels
%{_bindir}/modify-cmdline
%{_bindir}/postinstall
%{_bindir}/setup-audio
%{_sysconfdir}/eupnea/


%changelog
