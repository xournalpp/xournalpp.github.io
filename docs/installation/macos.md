---
template: installation/macos.html
title: MacOS Installation
hide:
  - navigation
  - toc
os_button: macos
compile_guide: https://github.com/xournalpp/xournalpp/blob/master/readme/MacBuild.md

version_class: windows-macos
versions:
  - name: Stable Intel
    subtitle: (Recommended for MacOS Intel users)
    description: Suits most users of older MacOS devices.
    links: macos.stable
    extras_ver: latest_stable
  - name: Stable ARM
    subtitle: (Recommended for MacOS ARM users)
    description: Suits most users with newer MacOS devices (M1, M2, ...).
    links: macos.stable-arm
    extras_ver: latest_stable
  - name: Nightly
    subtitle: (Unstable)
    description: Get new features as soon as they're implemented, in exchange for stability.
    links: nightly
    extras_ver: latest_unstable
---

You may see an error like this. Do the following to run Xournal++. [Click here](https://github.com/xournalpp/xournalpp/issues/6185) to learn why.

![MacOS quarantine error dialog](../img/installation/macOS_error.png){ .centered-image }

1. Download the dmg file.
2. Copy the Xournal++ program contained in the dmg file to the Applications
   folder by opening the dmg file and dragging the Xournal++ icon.
3. Open the Terminal and run `xattr -c /Applications/Xournal++.app` to remove quarantine. 
4. On MacOS Intel also run `codesign --force --deep --sign - /Applications/Xournal++.app` in the Terminal to self-sign the app. Note the hyphen after `--sign`.
5. Run Xournal++ like any other program.
6. Success!
