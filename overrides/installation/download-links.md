{% set default = "https://github.com/xournalpp/xournalpp/releases" %}
{% set allVersions = "https://github.com/xournalpp/xournalpp/releases" %}
{% set nightly = "https://github.com/xournalpp/xournalpp/releases/tag/nightly" %}
{% set windows =
    ({
        "stable" : "https://github.com/xournalpp/xournalpp/releases/download/v1.2.5/xournalpp-1.2.5-windows-setup-x86_64.exe"
    })
%}
{% set macos =
    ({
        "stable" : "https://github.com/xournalpp/xournalpp/releases/download/v1.2.5/xournalpp-1.2.5-macOS-X64.dmg",
        "stable-arm" : "https://github.com/xournalpp/xournalpp/releases/download/v1.2.5/xournalpp-1.2.5-macOS-ARM64.dmg"
    })
%}
{% set linux =
    ({
        "flatpak": "https://flathub.org/apps/details/com.github.xournalpp.xournalpp",
        "appimage": "https://github.com/xournalpp/xournalpp/releases/download/v1.2.5/xournalpp-1.2.5-x86_64.AppImage",
        "snap": "https://snapcraft.io/xournalpp",
        "debianStable": "https://github.com/xournalpp/xournalpp/releases/tag/v1.2.5",
        "ubuntuStable": "https://github.com/xournalpp/xournalpp/releases/tag/v1.2.5"
    })
%}
