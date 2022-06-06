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

    **(Ubuntu 22.04 and newer only or Debian testing)**: Install the latest
    stable release of Xournal++ from the official repositories:
    ```bash
    sudo apt update
    sudo apt install xournalpp
    ```

    **(Ubuntu-based distros only)**: Install the latest stable release from the
    following unofficial PPA
    ```bash
    sudo add-apt-repository ppa:apandada1/xournalpp-stable
    sudo apt update
    sudo apt install xournalpp
    ```
    
    **(Ubuntu-based distros only)**: Install the latest unstable nightly
    release from the following unofficial PPA
    ```bash
    sudo add-apt-repository ppa:andreasbutti/xournalpp-master
    sudo apt update
    sudo apt install xournalpp
    ```
    
    All of these can be easily upgraded via
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

    The latest stable release is available in nixpkgs as `xournalpp`, e.g.
    ```bash
    nix-shell -p xournalpp --run xournalpp
    ```

    To create a derivation for a development version, you can use
    [overlays](https://nixos.wiki/wiki/Overlays). Example overlay:
    ```nix
    self: super:
    {
      xournalpp = super.xournalpp.overrideAttrs (old: {
        # Override src with the version you want
        src = super.fetchFromGitHub {
          owner = "xournalpp";
          repo = "xournalpp";

          # Replace with the tag or commit hash you want
          rev = "v1.1.1";

          # Find the sha256 with:
          #   nix-prefetch-url --unpack --type sha256 <url of github tar gz>
          #
          # Example for 1.1.1:
          #   nix-prefetch-url --unpack --type sha256 https://github.com/xournalpp/xournalpp/archive/v1.1.1.tar.gz
          sha256 = "16pf50x1ps8dcynnvw5lz7ggl0jg7qvzv6gkd30xg3hkcxff8ch3";
        };
      });
    }
    ```

=== "Arch"

    Install the latest stable release via
    ```bash
    pacman -S xournalpp
    ```
    
    There is also a development package `xournalpp-git` available at https://aur.archlinux.org/packages/xournalpp-git/
