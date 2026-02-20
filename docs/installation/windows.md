---
template: installation/windows.html
title: Windows Installation
hide:
  - navigation
  - toc
os_button: windows
compile_guide: https://github.com/xournalpp/xournalpp/blob/master/readme/WindowsBuild.md

version_class: windows-macos
versions:
  - name: Stable Intel EXE
    subtitle: (Recommended - for Intel processors)
    description: Suits most users with its focus on stability.
    links: windows.stable
    extras_ver: latest_stable
  - name: Stable ARM EXE
    subtitle: (Recommended - for ARM processors)
    description: Suits most users with its focus on stability.
    links: windows.stable-arm
    extras_ver: latest_stable
  - name: Microsoft Store
    subtitle: (Recommended - for automatic updates)
    description: Suits most users with its focus on automatic updates of stable releases.
    links: windows.ms-store
  - name: Nightly EXE
    subtitle: (Unstable)
    description: Get new features as soon as they're implemented, in exchange for stability.
    links: nightly
    extras_ver: latest_unstable
---

=== "Direct Download"

    1. Unzip archive which should be named something like `xournalpp-{version}-windows.zip`
    2. Run the setup program contained in `xournalpp-{version}-windows.zip`
    3. Follow the installation steps
    4. Success!

=== "Scoop"
    With Scoop you can download the official release and keep it updated.
    Open Windows PowerShell and install the latest stable release via
    ```cmd
    scoop bucket add extras
    scoop install extras/xournalpp
    ```

=== "Winget"
    With Winget you can download the official release and keep it updated.
    Open Windows PowerShell and install the latest stable release via
    ```cmd
    winget install -e --id Xournal++.Xournal++
    ```
