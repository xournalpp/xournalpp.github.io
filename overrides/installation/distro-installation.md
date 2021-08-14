{% set distro_list = 
    [
        ({
            "internal_label": "Ubuntu",
            "tab_name": "Ubuntu and derivatives",
            "content":
                [
                    ({
                        "caption": "Install the latest stable release from the following unofficial ppa",
                        "code_line": [
                            "sudo add-apt-repository ppa:apandada1/xournalpp-stable",
                            "sudo apt update",
                            "sudo apt install xournalpp"
                        ]
                    }),
                    ({
                        "caption": "Install the latest unstable nightly release from the following unofficial ppa",
                        "code_line": [
                            "sudo add-apt-repository ppa:andreasbutti/xournalpp-master",
                            "sudo apt update",
                            "sudo apt install xournalpp"
                        ]
                    }),
                    ({
                        "caption": "Both of these can be easily upgraded via",
                        "code_line": [
                            "sudo apt update && sudo apt upgrade"
                        ]
                    })
                ]
        }),
        ({
            "internal_label": "Fedora",
            "tab_name": "Fedora",
            "content":
                [
                    ({
                        "caption": "Install the latest stable release via",
                        "code_line": [
                            "dnf install xournalpp"
                        ]
                    })
                ]
        }),
        ({
            "internal_label": "Solus",
            "tab_name": "Solus",
            "content":
                [
                    ({
                        "caption": "Install the latest stable release via",
                        "code_line": [
                            "sudo eopkg it xournalpp"
                        ]
                    })
                ]
        }),
        ({
            "internal_label": "openSUSE",
            "tab_name": "openSUSE",
            "content":
                [
                    ({
                        "caption": "Install the latest stable release via",
                        "code_line": [
                            "zypper in xournalpp"
                        ]
                    })
                ]
        }),
        ({
            "internal_label": "NIX",
            "tab_name": "NIXOS/NIX",
            "content":
                [
                    ({
                        "caption": "Install the latest stable release via",
                        "code_line": [
                            "nix-env -iA nixpkgs.xournalpp"
                        ]
                    })
                ]
        }),
        ({
            "internal_label": "Arch",
            "tab_name": "Arch",
            "content":
                [
                    ({
                        "caption": "Install the latest stable release via",
                        "code_line": [
                            "pacman -S xournalpp"
                        ]
                    })
                ]
        })
    ]
%}

{% macro instruction_generator(instruction_content) -%}
    <div class="instruction">
        <p>{{instruction_content.caption }}</p>
        <div class="code-instruction">
            <code>
            {% for code_line in instruction_content.code_line %}
                {{code_line}}<br>
            {% endfor %}
            </code>
        </div>
    </div>
{%- endmacro %}

{% macro distro_tab_generator(distro_tab_properties) -%}
    <input name="__tabbed_1" type="radio" id="__tabbed_1_{{distro_tab_properties.internal_label}}" checked="checked">
    <label for="__tabbed_1_{{distro_tab_properties.internal_label}}">{{distro_tab_properties.tab_name}}</label>
    <div class="tabbed-content">
        {% for instruction in distro_tab_properties.content %}
            {{ instruction_generator(instruction) }}
        {% endfor %}
    </div>
{%- endmacro %}


<div class="distro-list">
    <div class="tabbed-set">
        {% for distro in distro_list %}
            {{ distro_tab_generator(distro) }}
        {% endfor %}
    </div>
</div>