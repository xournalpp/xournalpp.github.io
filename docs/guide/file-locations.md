# Where to find Xournal++ files

When you download and install Xournal++ you may wonder where all the files get stored. Note that you can store your own Xournal++ documents (`.xopp`-files) wherever you like (up to file permissions).
Typically you would store them somewhere in your user folder. Autosave files get stored at the same location, just with a `.xopp~`-ending, once the `xopp-file` has been stored. So `abc.xopp` will be autosaved under `abc.xopp~`.  
This section explains where files get stored automatically either during installation or while using Xournal++. The following table provides an overwiew, detailing typical file locations:

|                                                     | Linux (.deb installer)           | MacOS (.app-bundle)                    | MS Windows (.exe installer)                                                |
|-----------------------------------------------------|----------------------------------|----------------------------------------|----------------------------------------------------------------------------|
| [Binary folder](#binary-folder)                     | `/usr/share/bin`                 | `Xournal++.app/MacOS`                  | `C:\Programs\Xournal++\bin`                                                |
| [Shared resources folder](#shared-resources-folder) | `/usr/share/xournalpp`           | `Xournal++.app/Resources`              | `C:\Programs\Xournal++\share\xournalpp`                                    |
| [Localizations folder](#localizations-folder)       | `/usr/share/locale`              | `Xournal++.app/Resources/share/locale` | `C:\Programs\Xournal++\share\locale`                                       |
| [Config folder](#config-folder)                     | `/home/<user>/.config/xournalpp` | `/Users/<user>/.config/xournalpp`      | `C:\Users\<user>\AppData\Local\xournalpp`                                  |
| [Cache folder](#cache-folder)                       | `/home/<user>/.cache/xournalpp`  | `/Users/<user>/.cache/xournalpp`       | `C:\Documents and Settings\<user>\Local Settings\Temporary Internet Files` |
| [Temporary folder](#temporary-folder)               | `/tmp`                           | `/tmp`                                 | `C:\Users\<user>\AppData\Local\Temp`                                       |

In accordance with the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/ar01s02.html) the *Config Folder* and *Cache Folder* can be defined by the environment
variables **$XDG_CONFIG_HOME** and **$XDG_CACHE_HOME**, respectively. The *Temporary folder* can be defined by **$TMPDIR** on Linux/MacOS or **$TEMP$** on MS Windows.
Below the contents of all the tabulated folders are explained. Some platform specific files not tabulated here are summarized [at the end](#platform-specific-files) of this section.

## Binary folder

The binary folder contains the executables for running Xournal++. On Linux and MacOS a thumbnailer is included for generating thumbnails in the file manager.

## Shared resources folder

The resources folder contains:

- the LaTeX templates (under Linux and Windows in the `resources` subfolder)
- `plugins` subfolder, containing all Lua plugins
- `ui` subfolder, containing
    - all `.glade` files, defining the user interface,
    - all Xournal++ icons, including the application icon and all toolbar icons
    - the toolbar configuration file `toolbar.ini`
    - the pagetemplates configuration file `pagetemplates.ini`
    - the css-style file `xournalpp.css`

## Localizations folder

The localizations folder contains the translations of Xournal++ in all supported languages. These are stored in files named `xournalpp.mo`

## Config folder

The config folder contains configuration files like

- the `settings.xml` file, which stores Xournal++ settings
- `autosave` subfolder for documents that have not been stored previously
- `metadata` subfolder, which contains metadata of previously opened files
- the `colornames.ini` file, which allows to configure colors

## Cache folder

The cache folder contains the `errorlogs` subfolder, which stores crash logs.

## Temporary folder

Temporary files generated by the LaTeX tool get stored in the temporary folder.

## Platform specific files

Some files installed by Xournal++ are platform-specific and are not contained on all platforms.

- On **Linux**: there are a desktop file, a copyright file, a changelog, man pages, metainfo and mime type files. The full list of files and file paths of a Xournal++ installation can be obtained in the terminal via `dpkg -L xournalpp`
- On **MacOS**: there are an `Info.plist`, a `pkginfo` and a `xournalpp.icns` icon for the `.app`-bundle, Adwaita and hicolor icons themes, diverse libraries (`.dylib`'s) and folders related to gtk/gdk and glib
- On **MS Windows**: there is an uninstaller `Uninstall.exe`, diverse libraires (`.dll`'s), Adwaita and hicolor icons themes and folders related to gtk/gdk and glib