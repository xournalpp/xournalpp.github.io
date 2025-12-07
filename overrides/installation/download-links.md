{% set default = "https://github.com/xournalpp/xournalpp/releases" %}
{% set allVersions = "https://github.com/xournalpp/xournalpp/releases" %}
{% set nightly = "https://github.com/xournalpp/xournalpp/releases/tag/nightly" %}
{% set windows =
    ({
        "stable" : "https://github.com/xournalpp/xournalpp/releases/download/v1.2.10/xournalpp-1.2.10-windows-setup-AMD64.exe",
        "stable-arm" : "https://github.com/xournalpp/xournalpp/releases/download/v1.2.10/xournalpp-1.2.10-windows-setup-ARM64.exe"
    })
%}
{% set macos =
    ({
        "stable" : "https://github.com/xournalpp/xournalpp/releases/download/v1.2.10/xournalpp-1.2.10-macOS-X64.dmg",
        "stable-arm" : "https://github.com/xournalpp/xournalpp/releases/download/v1.2.10/xournalpp-1.2.10-macOS-ARM64.dmg"
    })
%}
{% set linux =
    ({
        "flatpak": "https://flathub.org/apps/details/com.github.xournalpp.xournalpp",
        "appimage": "https://github.com/xournalpp/xournalpp/releases/download/v1.2.10/xournalpp-1.2.10-x86_64.AppImage",
        "snap": "https://snapcraft.io/xournalpp",
        "debianStable": "https://github.com/xournalpp/xournalpp/releases/tag/v1.2.10",
        "ubuntuStable": "https://github.com/xournalpp/xournalpp/releases/tag/v1.2.10"
    })
%}
