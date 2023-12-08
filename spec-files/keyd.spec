Name:       keyd
Version:    10.0.42
Release:    1%{?dist}
Summary:    A key remapping daemon for linux.
License:    MIT AND BSD-3-Clause
Url:    https://github.com/rvaiya/keyd
ExclusiveArch:   x86_64
# Add builddeps

%description
Made by rvaiya and repackaged by the Eupnea Project.
Pulls from the master branch instead of using latest release.

%prep
git clone --depth=1 https://github.com/rvaiya/keyd.git keyd-remote
git clone --depth=1 --branch=main https://github.com/eupnea-project/rpm-repo.git
git clone --depth=1 https://github.com/eupnea-project/eupnea-utils.git
git clone --depth=1 https://github.com/weirdtreething/chromebook-linux-audio.git


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
cp -r eupnea-utils/configs/keyboard-layouts %{buildroot}/%{_datadir}/eupnea/

# add generations json
cp chromebook-linux-audio/conf/boards.json %{buildroot}/%{_datadir}/eupnea/board-generations.json

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

# Enable keyd service
systemctl enable keyd.service

# use systemd-detect-virt to detect if in chroot -> if not in chroot, set keymap and start keyd
# systemd-detect-virt -r returns 1 if not in a chroot
systemd-detect-virt -r || /usr/lib/eupnea/set-keymap --automatic && systemctl start keyd.service