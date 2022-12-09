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
mkdir -p %{buildroot}/%{_libdir}/eupnea
mkdir -p %{buildroot}/%{_sysconfdir}/eupnea

# Copy scripts to bin
install -m 755 postinstall-scripts/user-scripts/* %{buildroot}/%{_bindir}/
install -m 755 audio-scripts/setup-audio %{buildroot}/%{_bindir}/

# Copy scripts to lib
cp postinstall-scripts/system-scripts/* %{buildroot}/%{_libdir}/eupnea/
cp postinstall-scripts/functions.py %{buildroot}/%{_libdir}/eupnea/

cp -r postinstall-scripts/configs/* %{buildroot}/%{_sysconfdir}/eupnea/
cp -r audio-scripts/configs/* %{buildroot}/%{_sysconfdir}/eupnea/

%files
%{_bindir}/collect-logs
%{_bindir}/install-to-internal
%{_bindir}/manage-kernels
%{_bindir}/modify-cmdline
%{_bindir}/setup-audio

%{_libdir}/eupnea/*

%{_sysconfdir}/eupnea/*

%changelog