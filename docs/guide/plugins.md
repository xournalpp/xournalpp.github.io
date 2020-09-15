# Plugins

Xournal++ provides a basic Lua Plugin interface. Plugins can be added without building Xournal++ from source. Their primary use is to add user-specific functionality, shortcuts, make calls to external programs, define user-specific export functions and the like.

In general the Lua Plugin interface is still in a very early stage and does not provide
much functionality, but it can still be quite useful at times.

In order to use Lua Plugins make sure you have `Lua (version >=5.3)` installed on your device.

## Plugin manager

Plugins must be activated or deactivated in the Plugin manager (from the menubar). The Plugin manager lists the installation folder, description, author and version for each plugin. Only activated plugins will be listed in the menubar and only those can be run. The other plugins are safely excluded. Note that a restart of Xournal++ is required to change the activation of a plugin.

## Installation folder

Currently all plugins reside in the same folder. By default this folder is

- `/usr/local/share/xournalpp/plugins/` under Linux. 
- `C:\Program Files\Xournal++\plugins\` under Windows.

Each plugin has its files stored in a subfolder of the plugin folder and contains at least a `plugin.ini` file and a Lua code file.

Custom plugin folder(s) are planned to be added, see [this issue](https://github.com/xournalpp/xournalpp/issues/1155), but not yet there.

## Plugin structure

The `plugin.ini` file contains the name of the author, the version number, info on whether it is enabled by default
or not and a reference to the main Lua code file. A sample file (referencing `main.lua`) is:

#### **`plugin.ini`**
```ini 
[about]
## Author / Copyright notice
author=NAME OF THE AUTHOR

description=DESCRIPTION OF THE PLUGIN

## If the plugin is packed with Xournal++, use
## <xournalpp> then it gets the same version number
version=<xournalpp>

[default]
enabled=false

[plugin]
mainfile=main.lua

```

The Lua code file referenced in the `plugin.ini` file must define a `initUi`-function that registers toolbar actions and initializes all UI stuff. It is supposed to call the `app.registerUi`-function, whose argument is a Lua table containing 

- the `menu` name displayed in Xournal++'s menubar,
- the `callback` function used when the plugin is called from the menu or via accelerator,
- the `accelerator` used to execute the plugin callback function. The format looks like `<Control>a` or `<Shift><Alt>F1` or `<Release>z` (for key release). See [GTK3 reference](https://developer.gnome.org/gtk3/stable/gtk3-Keyboard-Accelerators.html#gtk-accelerator-parse) for details. The accelerator can be omitted.

A sample file for the main Lua code file is:

#### **`main.lua`**
```lua 
-- Register all Toolbar actions and intialize all UI stuff
function initUi()
  app.registerUi({["menu"] = "NAME", ["callback"] = "run", ["accelerator"] = "<Alt>F1"});
-- ADD MORE CODE, IF NEEDED
end

-- Callback if the menu item is executed
function run()
-- ADD CODE
end

``` 

## Plugin API 

The Lua Plugin can execute a (small) number of Xournal++ functions to interact with Xournal++. Those are defined in the 
[Plugin API](https://github.com/xournalpp/xournalpp/blob/master/src/plugin/luapi_application.h#L237-L242?)

Currently the list contains the following functions:

- `app.msgbox` for displaying messages to the user and letting the user choose an option by clicking a button
- `app.registerUi` used in the `initUi`-function
- `app.uiAction` for simulating a toolbar/menubar click starting some action,
- `app.uiActionSelected` for simulating a toolbar/menubar click making a selection,
- `app.changeCurrentPageBackground` for changing the background of the current page,
- `app.saveAs` for retrieving the filename from a native saveAs dialog.

Two more functions are currently been added to the API in a [Pull Request for handwriting recognition](https://github.com/xournalpp/xournalpp/pull/2176). 

- `app.getStrokes` gets the strokes from the selection tool or a page layer
- `app.getWidthAndHeight` gets the width and the height from the selection tool or a page layer

Future progress on the Plugin API will be reported here. Help is always welcome.


## Using Lua modules

More complex Plugins will require Lua modules for certain operations. For instance if your Plugin needs a more sophisticated GUI, you may want to use the `lgi`-module via ```require("lgi")```. 

For security reasons the Lua package path currently only contains the folder of the plugin. So you must add the path where the Lua modules you use are installed. This can be done by executing:

```lua
package.path = package.path .. "YOUR PATH(S)"
``` 
in the `initUI`-function. 

## Notable Plugins

- The `QuickSnapshot` Plugin uses an external screenshot tool, to quickly take a screen snapshot of a region of the screen and save it into a user specified file
- The `ToggleGrid` Plugin provides a shortcut for toggling between "grid background with snapping to grid" and "plain background without snapping to grid"
- The `HandwritingRecognition` Plugin (work in progress) uses the google cloud-based IME handwriting API to recognize handwritten text from a selection or page layer in a user-specified language.

