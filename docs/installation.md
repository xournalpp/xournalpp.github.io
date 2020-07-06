# Installation Guide

The official releases of Xournal++ can be found on the
[Releases](https://github.com/xournalpp/xournalpp/releases) page. We provide
binaries for Debian (Buster), Ubuntu (16.04), MacOS (10.13 and newer), and
Windows. For other Linux distributions (or older/newer ones), we also provide an
AppImage that is binary compatible with any distribution released around or
after Ubuntu 16.04.

On Linux, Xournal++ can also be installed via [snapcraft](https://snapcraft.io/xournalpp).

**A note for Ubuntu/Debian users**: The official binaries that we provide are
only compatible with the _specific version of Debian or Ubuntu_ indicated by the
file name. For example, if you are on Ubuntu 20.04, the binary whose name
contains `Ubuntu-xenial` is _only_ compatible with Ubuntu 18.04. If your system
is not one of the specific Debian or Ubuntu versions that are supported by the
official binaries, we recommend you use either the PPA, the Flatpak, or the
AppImage.

There is also an _unstable_, [automated nightly
release](https://github.com/xournalpp/xournalpp/releases/tag/nightly) that
includes the very latest features and bug fixes.

With the help of the community, Xournal++ is also available on official repositories
of some popular Linux distros and platforms.

### Ubuntu and derivatives

An _unstable_, nightly release is available for Ubuntu-based distributions via the following PPA:

```bash
sudo add-apt-repository ppa:andreasbutti/xournalpp-master
sudo apt update
sudo apt install xournalpp
```

This PPA is provided by the Xournal++ team. While it has the latest features and
bug fixes, it has also not been tested thoroughly and may break periodically (we
try our best not to break things, though).

We eventually also planning on setting up a PPA for stable releases
([#1013](https://github.com/xournalpp/xournalpp/issues/1013)).

### Fedora

The [released version of
xournalpp](https://src.fedoraproject.org/rpms/xournalpp) is available in the
[main repository](https://bodhi.fedoraproject.org/updates/?packages=xournalpp)
via _Software_ application or the following command:

```bash
sudo dnf install xournalpp
```
or 
```bash
pkcon install xournalpp
```

The bleeding edge packages synced to xournalpp git master on a daily basis are available from [COPR luya/xournalpp](https://copr.fedorainfracloud.org/coprs/luya/xournalpp/).
[![Copr build status](https://copr.fedorainfracloud.org/coprs/luya/xournalpp/package/xournalpp/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/luya/xournalpp/package/xournalpp/)

### openSUSE

On openSUSE Tumbleweed, the released version of Xournal++ is available from the
main repository:

```bash
sudo zypper in xournalpp
```

For openSUSE Leap 15.0 and earlier, use the install link from
[X11:Utilities](https://software.opensuse.org//download.html?project=X11%3AUtilities&package=xournalpp).

For all versions of openSUSE, bleeding edge packages synced to xournalpp git
master on a weekly basis are available from
[home:badshah400:Staging](https://software.opensuse.org//download.html?project=home%3Abadshah400%3AStaging&package=xournalpp).

### Arch Linux

The latest stable release is available [in the [extra]
repository](https://www.archlinux.org/packages/?q=xournalpp).

To build the latest state of the master branch yourself, use [this AUR
package](https://aur.archlinux.org/packages/xournalpp-git/).

### Solus

The latest stable release is available in the main repository:

```bash
sudo eopkg it xournalpp
```

### Flatpak

The Xournal++ team officially supports a [FlatHub
release](https://flathub.org/apps/details/com.github.xournalpp.xournalpp), which
can be installed with

```bash
flatpak install flathub com.github.xournalpp.xournalpp
```

Note that for Xournal++ to work properly, you must have at least one GTK theme
and one icon theme installed on Flatpak. To enable LaTeX support, you will also
need to install the TeX Live extension:

```bash
flatpak install flathub org.freedesktop.Sdk.Extension.texlive
```

The Flatpak manifest can be found at the [Xournal++ Flatpak packaging
repository](https://github.com/flathub/com.github.xournalpp.xournalpp), and all
Flatpak-related packaging issues should be reported there.

### Windows

Official Windows releases are provided on the [Releases
page](https://github.com/xournalpp/xournalpp/releases).

**Notes:**

* Currently, only WinTab drivers are supported. This is due to a limitation with
  the underlying library that we use, GTK.
* There is a GTK that prevents stylus input from working correctly. Please start
  Xournal++, touch with the stylus, quit Xournal++ and start again. Then stylus
  input will be working, until you restart Windows. See
  [#659](https://github.com/xournalpp/xournalpp/issues/659).

### Mac OS X

Mac OS X releases are provided on the [Releases
page](https://github.com/xournalpp/xournalpp/releases).

**Notes:**

* There have been compatibility problems with Mac OS X Catalina regarding both
  file permissions and stylus support
  ([#1772](https://github.com/xournalpp/xournalpp/issues/1772) and
  [#1757](https://github.com/xournalpp/xournalpp/issues/1757)). Unfortunately,
  we don't have the resources to adequately support Catalina at this time. Help
  would be appreciated!
* Xournal++ will be delivered with a patched GTK. Else pressure sensitivity may
  not will not work on Mac
  [#569](https://github.com/xournalpp/xournalpp/issues/569).

