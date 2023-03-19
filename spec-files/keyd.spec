Name:       keyd
Version:    10.0.1
Release:    1%{?dist}
Summary:    A key remapping daemon for linux.
License:    MIT
Url:    https://github.com/rvaiya/keyd
ExclusiveArch:   x86_64

%description
Made by rvaiya and repackaged by the Eupnea Project.
Pulls from the master branch instead of using latest release.

%prep
git clone --depth=1 https://github.com/rvaiya/keyd.git keyd-remote

%build

%install
# Make dirs
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/%{_datadir}/libinput
# the other dirs are automatically created by make install

# Install with make
# TODO: move to %build
cd keyd-remote
make
make DESTDIR=%{buildroot} PREFIX='/usr' install
cd ..

%files
%{_bindir}/keyd
%{_bindir}/keyd-application-mapper

/usr/lib/systemd/system/keyd.service

%{_sysconfdir}/keyd # empty dir

%{buildroot}/%{_datadir} # lots of dirs

%post
#!/bin/sh

# Add keyd to groups
groupadd keyd

# Enable and start keyd
systemctl enable --now keyd