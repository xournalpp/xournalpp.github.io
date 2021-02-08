# Linux installation

## General information

Xournal++ is a free and open source program and can be easily compiled from source, although for user convenience it is also distributed via precompiled binary. In case you want to compile xournalpp on your own you should follow the guide on the [github page](https://github.com/xournalpp/xournalpp/blob/master/readme/LinuxBuild.md). If you decide to do otherwise, then this guide is dedicated to that process.

## Options for all/most distros

The following options are available on most major Linux distros.

<ul id="linuxDownloadsContainer" class="downloadsContainer">
<a class="xournalppButton downloadButton" href="{{downloads.linux.appimage}}">AppImage</a>
<a class="xournalppButton" href="{{downloads.linux.flatpak}}">FlatPak</a>
<a class="xournalppButton " href="{{downloads.linux.snap}}">Snap Package</a>
<a class="xournalppButton" href="{{downloads.allVersions}}">Other versions</a>
<a class="xournalppButton" style="grid-column: 1 / 3;" href="{{downloads.nightly}}">Nightly (including nightly AppImage)</a>
<a class="xournalppButton" style="grid-column: 3 / 5;" href="#options-for-specific-distros-potentially-preferable">Or use distro specific method</a>
</ul>

## Options for specific distros (potentially preferable)

On _specific Linux distros_ you have the following extra options:

### Ubuntu and derivatives

* Install the latest *unstable* nightly release from the following ppa
  
        sudo add-apt-repository ppa:andreasbutti/xournalpp-master
        sudo apt update
        sudo apt install xournalpp

    which you can easily upgrade via `sudo apt update && sudo apt upgrade`

* Install the latest *stable* release from the following *unofficial* ppa

        sudo add-apt-repository ppa:apandada1/xournalpp-stable
        sudo apt update
        sudo apt install xournalpp

* Install the latest stable release (currently version {{ version.latest_stable }}) from the [releases page](https://github.com/xournalpp/xournalpp/releases)
* Install the latest unstable release (automated nightly build) from the [releases page]({{downloads.nightly}})

### Debian Buster

* Install the latest stable release (version {{ version.latest_stable }}) from the [releases page](https://github.com/xournalpp/xournalpp/releases/tag/1.0.20-hotfix)
* Install the latest unstable release (automated nightly build) from the [releases page]({{downloads.nightly}})

### Fedora

Install the latest stable release via

    dnf install xournalpp

### openSuse

Install the latest stable release via

    zypper in xournalpp

### Solus

Install the latest stable release via

    sudo eopkg it xournalpp

### Arch

Install the latest stable release from the _community_ repository via
  
    pacman -S xournalpp 
 
### NixOS/Nix

Install the latest stable release via

    nix-env -iA nixpkgs.xournalpp
