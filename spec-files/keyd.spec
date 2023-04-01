Name:       keyd
Version:    10.0.17
Release:    1%{?dist}
Summary:    A key remapping daemon for linux.
License:    MIT
Url:    https://github.com/rvaiya/keyd
ExclusiveArch:   x86_64
# Add builddeps

%description
Made by rvaiya and repackaged by the Eupnea Project.
Pulls from the master branch instead of using latest release.

%prep
git clone --depth=1 https://github.com/rvaiya/keyd.git keyd-remote
git clone --depth=1 --branch=main https://github.com/eupnea-linux/rpm-repo.git
git clone --depth=1 https://github.com/eupnea-linux/eupnea-utils.git

%build
cd keyd-remote
make

%install
# Make dirs
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/%{_datadir}/libinput
mkdir -p %{buildroot}/%{_datadir}/eupnea
# the other dirs are automatically created by make install

# Install with make
cd keyd-remote
make DESTDIR=%{buildroot} PREFIX='/usr' install
cd ..

# add quirks file
cp rpm-repo/configs/keyd.quirks %{buildroot}/%{_datadir}/libinput/keyd.quirks

# add keyboard configs
cp -r eupnea-utils/configs/* %{buildroot}/%{_datadir}/eupnea/

%files
%{_bindir}/keyd
%{_bindir}/keyd-application-mapper

/usr/lib/systemd/system/keyd.service

%dir %{_sysconfdir}/keyd

/%{_datadir}/*

%post
#!/bin/sh

# Add keyd to groups
groupadd keyd

# Enable and start keyd
systemctl enable --now keyd
