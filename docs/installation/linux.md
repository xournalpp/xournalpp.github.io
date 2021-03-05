# Linux installation

## General information

Xournal++ is a free and open source program and can be easily compiled from source, although for user convenience it is also distributed via precompiled binary. In case you want to compile xournalpp on your own you should follow the guide on the [github page](https://github.com/xournalpp/xournalpp/blob/master/readme/LinuxBuild.md). If you decide to do otherwise, then this guide is dedicated to that process.

## Options for all/most distros

The following options are available on most major Linux distros.

<ul id="linuxDownloadsContainer" class="downloadsContainer">
<li><a class="xournalppButton downloadButton" href="{{downloads.linux.appimage}}">AppImage</a></li>
<li><a class="xournalppButton linkButton" href="{{downloads.linux.flatpak}}">FlatPak</a></li>
<li><a class="xournalppButton linkButton" href="{{downloads.linux.snap}}">Snap Package</a></li>
<li><a class="xournalppButton linkButton" href="{{downloads.allVersions}}">Other versions</a></li>
<li><a class="xournalppButton linkButton" href="{{downloads.nightly}}">Nightly (latest unstable, including nightly AppImage)</a></li>
<li><a class="xournalppButton linkButton" href="#options-for-specific-distros-potentially-preferable">Or use distro specific method</a></li>
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

* Or:
<ul id="ubuntuContainer" class="downloadsContainer">
<li><a class="xournalppButton linkButton" href="{{downloads.linux.ubuntuStable}}">Download stable</a></li>
<li><a class="xournalppButton linkButton" href="{{downloads.nightly}}">Download nightly (latest unstable) version</a></li>
<li><a class="xournalppButton linkButton" href="{{downloads.allVersions}}">Other versions</a></li>
</ul>

### Debian Buster

<ul id="debianContainer" class="downloadsContainer">
<li><a class="xournalppButton linkButton" href="{{downloads.linux.debianStable}}">Download stable</a></li>
<li><a class="xournalppButton linkButton" href="{{downloads.nightly}}">Download nightly (latest unstable) version</a></li>
<li><a class="xournalppButton linkButton" href="{{downloads.allVersions}}">Other versions</a></li>
</ul>

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
