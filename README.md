# rpm-repo

Repo for Fedora rpm packages. Provides the following packages:

* `eupnea-utils`: Packaged eupnea scripts from the [utils](https://github.com/eupnea-project/eupnea-utils)
  and [audio](https://github.com/eupnea-project/audio-scripts/) repos.
* `eupnea-system`: Does not install anything per se, but instead includes a postinstall hook, which
  executes [system-update.py](https://github.com/eupnea-project/system-update) to upgrade between Depthboot/EupneaOS
  versions.
* `eupnea-mainline-kernel` + `modules` + `headers`: Mainline kernel, modules and headers.
  See [eupnea-mainline-kernel](https://eupnea-project.github.io/docs/project/kernels#mainline-eupnea-kernel)
* `eupnea-chromeos-kernel` + `modules` + `headers`: ChromeOS kernel, modules and headers.
  See [eupnea-chromeos-kernel](https://eupnea-project.github.io/docs/project/kernels#chromeos-eupnea-kernel)
* `keyd`: A key remapping daemon for linux, made by rvaiya. See [keyd](https://github.com/rvaiya/keyd)
* `depthboot-logo`: [Alpine busybox-static](https://dl-cdn.alpinelinux.org/alpine/v3.17/main/x86_64/busybox-static-1.35.0-r29.apk) +
  Depthboot logo boot splash systemd service.
* `eupneaos-logo`: [Alpine busybox-static](https://dl-cdn.alpinelinux.org/alpine/v3.17/main/x86_64/busybox-static-1.35.0-r29.apk) +
  EupneaOS logo boot splash systemd service.

# Add to system

```
sudo dnf config-manager --add-repo https://eupnea-project.github.io/rpm-repo/eupnea.repo
sudo dnf update --refresh
sudo dnf install eupnea-utils eupnea-system
```
