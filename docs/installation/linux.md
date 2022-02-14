---
template: installation/linux.html
title: Linux Installation
hide:
  - navigation
  - toc
os_button: linux
compile_guide: https://github.com/xournalpp/xournalpp/blob/master/readme/LinuxBuild.md

choose_subtitle: "Pre-built packages are available for Debian, Ubuntu and derivatives, and most distros"

version_class: linux
versions:
  - name: Stable
    subtitle: (Recommended)
    description: Suits most users with its focus on stability.
    extras_ver: latest_stable
    links: 
    - label: AppImage
      attr: linux.appimage
    - label: Flatpak
      attr: linux.flatpak
    - label: Snap
      attr: linux.snap
    - label: ".deb"
      attr: linux.debianStable
  - name: Nightly
    subtitle: (Unstable)
    description: Get new features as soon as they're implemented, in exchange for stability.
    extras_ver: latest_unstable
    links:
    - label: AppImage
      attr: nightly
    - label: ".deb"
      attr: nightly
---

=== "Ubuntu and derivatives"

    Install the latest stable release from the following unofficial PPA
    ```bash
    sudo add-apt-repository ppa:apandada1/xournalpp-stable
    sudo apt update
    sudo apt install xournalpp
    ```
    
    Install the latest unstable nightly release from the following unofficial PPA
    ```bash
    sudo add-apt-repository ppa:andreasbutti/xournalpp-master
    sudo apt update
    sudo apt install xournalpp
    ```
    
    Both of these can be easily upgraded via
    ```bash
    sudo apt update && sudo apt upgrade
    ```

=== "Fedora"
    
    Install the latest stable release via
    ```bash
    dnf install xournalpp
    ```

=== "Solus"
    
    Install the latest stable release via
    ```bash
    sudo eopkg it xournalpp
    ```

=== "openSUSE"
    
    Install the latest stable release via
    ```bash
    zypper in xournalpp
    ```

=== "NixOS / Nix"

    Install the latest stable release via
    ```bash
    nix-env -iA nixpkgs.xournalpp
    ```

=== "Arch"

    Install the latest stable release via
    ```bash
    pacman -S xournalpp
    ```
    
    There is also a development package `xournalpp-git` available at https://aur.archlinux.org/packages/xournalpp-git/
