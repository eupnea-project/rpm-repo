Name:       keyd
Version:    10.0.16
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

%build
cd keyd-remote
make

%install
# Make dirs
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/%{_datadir}/libinput
# the other dirs are automatically created by make install

# Install with make
cd keyd-remote
make DESTDIR=%{buildroot} PREFIX='/usr' install
cd ..

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
