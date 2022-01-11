{% set default = "https://github.com/xournalpp/xournalpp/releases" %}
{% set allVersions = "https://github.com/xournalpp/xournalpp/releases" %}
{% set nightly = "https://github.com/xournalpp/xournalpp/releases/tag/nightly" %}
{% set windows = 
    ({
        "stable" : "https://github.com/xournalpp/xournalpp/releases/download/1.1.0-hotfix.1/xournalpp-1.1.0-hotfix.1-windows.zip"
    })
%}
{% set macos = 
    ({
        "stable" : "https://github.com/xournalpp/xournalpp/releases/download/1.1.0/xournalpp-1.1.0-macos.zip"
    })
%}
{% set linux = 
    ({
        "flatpak": "https://flathub.org/apps/details/com.github.xournalpp.xournalpp",
        "appimage": "https://github.com/xournalpp/xournalpp/releases/download/1.1.0/xournalpp-1.1.0-x86_64.AppImage",
        "snap": "https://snapcraft.io/xournalpp",
        "debianStable": "https://github.com/xournalpp/xournalpp/releases/tag/1.1.0",
        "ubuntuStable": "https://github.com/xournalpp/xournalpp/releases/tag/1.1.0"
    })
%}
