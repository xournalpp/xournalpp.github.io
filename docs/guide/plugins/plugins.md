# Building Plugins

Xournal++ provides a basic Lua Plugin interface. Plugins can be added without building Xournal++ from source. Their primary use is to add user-specific functionality, shortcuts, make calls to external programs, define user-specific export functions and the like.

In general the Lua Plugin interface is still in an early stage and will be expanded over time.

In order to use Lua Plugins make sure you have `Lua (version >=5.3)` installed on your device.

## Plugin manager

Plugins must be activated or deactivated in the Plugin manager (from the menubar). The Plugin manager lists the installation folder, description, author and version for each plugin. Only activated plugins will be listed in the menubar and only those can be run. The other plugins are safely excluded. Note that a restart of Xournal++ is required to change the activation of a plugin.

## Installation folder

Currently all plugins reside in the same folder. By default this folder is

- `/usr/share/xournalpp/plugins/` under Linux.
- `C:\Program Files\Xournal++\share\xournalpp\plugins\` under MS Windows.
- `Contents/Resources/plugins` inside the `Xournal++.app` bundle under MacOS.

Each plugin has its files stored in a subfolder of the plugin folder and contains at least a `plugin.ini` file and a Lua code file.

Custom plugin folder(s) are planned to be added, see [this pull request](https://github.com/xournalpp/xournalpp/pulls/2422), but not yet there.

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

The Lua code file referenced in the `plugin.ini` file must define an `initUi`-function that registers toolbar actions and initializes all UI stuff. It is supposed to call the `app.registerUi`-function, whose argument is a Lua table containing

- the `menu` name displayed in Xournal++'s menubar,
- the `callback` function used when the plugin is called from the menu or via a keyboard accelerator,
- the `accelerator` used to execute the plugin callback function. The format looks like `<Control>a` or `<Shift><Alt>F1` or `<Release>z` (for key release). See [GTK3 reference](https://developer.gnome.org/gtk3/stable/gtk3-Keyboard-Accelerators.html#gtk-accelerator-parse) for details and note that release key accelerators currently do not work, see [this issue](https://github.com/xournalpp/xournalpp/issues/2396). The accelerator can be omitted. Using accelerators without modifiers like (`<Alt>`, `<Control>`, `<Shift>`) is allowed, but will likely break the text tool.

You can register multiple menu entires/accelators in the same plugin by using `app.registerUi` multiple times.

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
-- ADD CODE LIKE
-- app.uiAction({["action"]="ACTION_TOOL_PEN"})
-- TO SWITCH TO THE PEN TOOL, OR
-- app.changeToolColor({["color"] = 0xff0000, ["selection"] = true})
-- TO CHANGE THE COLOR OF THE CURRENT TOOL TO RED
end

```

## Plugin API

The Lua Plugin can execute a number of Xournal++ functions to interact with Xournal++. Those are defined in the
[Plugin API](https://github.com/xournalpp/xournalpp/blob/a92fcac0273a39fe89beeeb88c14406864c10306/src/plugin/luapi_application.h#L742-L762).

Currently the list contains the following functions:

- `app.msgbox` for displaying messages to the user and letting the user choose an option by clicking a button
- `app.saveAs` for retrieving the filename from a native saveAs dialog.
- `app.registerUi` used in the `initUi`-function
- `app.uiAction` for simulating a toolbar/menubar click starting some action,
- `app.uiActionSelected` for notifying action listeners about selected options,
- `app.changeCurrentPageBackground` for changing the background of the current page,
- `app.sidebarAction` for actions accessible in the sidebar
- `app.layerAction` for actions accessible in the layer controller
- `app.changeToolColor` for changing the color of any tool with color capabilities,
- `app.changePdfBackgroundPageNr` to change the pdf background page number
- `app.getDocumentStructure` to get lots of useful info on the document, also used for applying operations on all/selected pages
- `app.scrollToPage`scrolls relatively or absolutely to a page
- `app.scrollToPos` scrolls relatively or absolutely to a new position on the same page
- `app.setCurrentPage` sets the given page as new current page
- `app.setPageSize` sets the width and height of the current page
- `app.setCurrentLayer` sets the given layer as the new current layer, and updates visibility if specified
- `app.setLayerVisibility` sets the visibility of the current layer

All those functions are documented in the same file [`luapi_application.h`](https://github.com/xournalpp/xournalpp/blob/master/src/plugin/luapi_application.h), including example usage. Future progress on the Plugin API will be reported here. Help is always welcome.

### Using plugins to define shortcuts for ui actions

Currently Xournal++ does not have shortcuts/keybindings configurable in the preferences. However you can write your custom plugin to achieve exactly that.

The function `app.uiAction` used for simulating a toolbar/menubar click can be used for lots of different actions.
This command accepts a Lua table with keys
`"action"`, `"group"` and `"enabled"`
as its argument. The `"group"` key is only used for displaying warnings, so you can omit it. The `"enabled"` key is set to `true` by default, so you can often omit it as well. The `"action"` key accepts
one of the action strings listed in the [`Control::actionPerformed` method](https://github.com/xournalpp/xournalpp/blob/6fa6d3c98e33ed71e31f9ef79de18b845cbd9c70/src/control/Control.cpp#L371-L968) in the source code. Note that the list of actions will change when new functionality is added to Xournal++.

For example use:

```lua
app.uiAction({["action"]="ACTION_RULER"})
```

to activate the ruler (for drawing line segments) or

```lua
app.uiAction({["action"]="ACTION_TOOL_FILL", ["enabled"]=false})
```

to turn off filling of shapes.

### Retrieving information about the document and iterating through pages and layers

The `app.getDocumentStructure` function yields a Lua table of the following shape:

```lua
{
  "pages" = {
    {
      "pageWidth" = number,
      "pageHeight" = number,
      "isAnnoated" = bool,
      "pageTypeFormat" = string,
      "pdfBackgroundPageNo" = integer (0, if there is no pdf background page),
      "layers" = {
        [0] = {
          "isVisible" = bool
        },
        [1] = {
          "isVisible" = bool,
          "isAnnotated" = bool
        },
        ...
      },
      "currentLayer" = integer
    },
  ...
  }
  "currentPage" = integer,
  "pdfBackgroundFilename" = string (empty if there is none)
}
```

So for example to get the number of all pages, the page number of the current page and the layer ID of the current layer use the code:

```lua
local docStructure = app.getDocumentStructure
local numPages = #docStructure["pages"]
local currPage = docStructure["currentPage"]
local currLayer = docStructure["pages"][currPage]["currentLayer"]
```

You can iterate through all pages by using the lines

```lua
local docStructure = app.getDocumentStructure
local numPages = #docStructure["pages"]
for i=1, numPages do
  -- ADD CODE TO EXECUTE FOR PAGE i
end

```

Similarly you can run through all layers of a page. In case of the current page this would read like

```lua
local docStructure = app.getDocumentStructure
local page = docStructure["currentPage"]
local numLayers = #docStructure["pages"][page]["layers"]
for i=1, numLayers do
  -- ADD CODE TO EXECUTE FOR LAYER i
end
```

## Using Lua modules

More complex Plugins will require Lua modules for certain operations. For instance if your Plugin needs a more sophisticated GUI, you may want to use the `lgi`-module via ```require("lgi")```.

The Lua package path by default contains the root folder of the plugin and the system Lua package path. In case you need other folders in the package path, use the package.path key to add them.
