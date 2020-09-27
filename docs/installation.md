# Installation Guide

On this page we summarize the main installation options. For more details see [the main page of the repository](https://github.com/xournalpp/xournalpp#Installing).

Depending on your operation system you mainly have the following options to install Xournal++ on your device.

## Windows

* Install the latest stable release (currently version 1.0.18) from the [releases page](https://github.com/xournalpp/xournalpp/releases)
* Install the latest unstable release (automated nightly build) from the [releases page](https://github.com/xournalpp/xournalpp/releases/tag/nightly)
* Bulid the latest development version (currently version 1.1.0+dev) from source as described on [this wiki page](https://github.com/xournalpp/xournalpp/blob/master/readme/WindowsBuild.md)

## MacOS

* Install the latest stable release (currently version 1.0.18) from the [releases page](https://github.com/xournalpp/xournalpp/releases)
* Install the latest unstable release (automated nightly build) from the [releases page](https://github.com/xournalpp/xournalpp/releases/tag/nightly)
* Bulid the latest development version (currently version 1.1.0+dev) from source as described on [this wiki page](https://github.com/xournalpp/xournalpp/blob/master/readme/MacBuild.md)

## Linux

### Options for all/most distros

The following options are available on _most major Linux distros.

* Install the Snap Package (currently version 1.0.16) from the [SnapCraft release](https://snapcraft.io/xournalpp)
* Install the FlatPak (currently version 1.0.18) from the [official FlatHub release](https://flathub.org/apps/details/com.github.xournalpp.xournalpp)
* Install the AppImage (latest stable release, currently 1.0.18) from the [releases page](https://github.com/xournalpp/xournalpp/releases)
* Bulid the latest development version (currently version 1.1.0+dev) from source as described on [this wiki page](https://github.com/xournalpp/xournalpp/blob/master/readme/LinuxBuild.md)

### Options for specific distros (potentially preferable)

On _specific Linux distros_ you have the following extra options:

#### Ubuntu and derivatives

Install the latest *unstable* nightly release from the following ppa
  
    sudo add-apt-repository ppa:andreasbutti/xournalpp-master
    sudo apt update
    sudo apt install xournalpp

which you can easily upgrade via `sudo apt update && sudo apt upgrade`

Install the latest *stable* release from the following *unofficial* ppa

    sudo add-apt-repository ppa:apandada1/xournalpp-stable
    sudo apt update
    sudo apt install xournalpp

* Install the latest stable release (currently version 1.0.18) from the [releases page](https://github.com/xournalpp/xournalpp/releases)
* Install the latest unstable release (automated nightly build) from the [releases page](https://github.com/xournalpp/xournalpp/releases/tag/nightly)

#### Debian Buster

* Install the latest stable release (currently version 1.0.18) from the [releases page](https://github.com/xournalpp/xournalpp/releases)
* Install the latest unstable release (automated nightly build) from the [releases page](https://github.com/xournalpp/xournalpp/releases/tag/nightly)

#### Fedora

Install the latest stable release via

    dnf install xournalpp

#### openSuse

Install the latest stable release via

    zypper in xournalpp

#### Solus

Install the latest stable release via

    sudo eopkg it xournalpp

#### Arch

Install the latest stable release from the _extra_ repository via
  
    pacman -S xournalpp 
  