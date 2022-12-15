# rpm-repo

Repo for Fedora rpm packages. Provides the following packages:

* `eupnea-utils`: Packaged eupnea scripts from the [postinstall](https://github.com/eupnea-linux/postinstall-scripts)
  and [audio](https://github.com/eupnea-linux/audio-scripts/) repos.
* `eupnea-system`: Does not install anything per se, but instead includes a postinstall hook, which
  executes [system-update.py](https://github.com/eupnea-linux/system-update) to upgrade between Depthboot/EupneaOS
  versions.

# Add to system

```
sudo dnf config-manager --add-repo https://eupnea-linux.github.io/rpm-repo/eupnea.repo
sudo dnf update --refresh
sudo dnf install eupnea-utils eupnea-system
```
