# Building Plugins

Xournal++ provides a basic Lua Plugin interface. Plugins can be added without building Xournal++ from source. Their primary use is to add user-specific functionality, shortcuts, make calls to external programs, define user-specific export functions and the like.

In general the Lua Plugin interface is still in an early stage and will be expanded over time.

In order to use Lua Plugins make sure you have `Lua (version >=5.3)` installed on your device.

## Plugin manager

Plugins must be activated or deactivated in the Plugin manager (from menu `Plugin > Plugin manager`). The Plugin manager lists the installation folder, description, author and version for each plugin. Only activated plugins will be listed in the menubar and only those can be run. The other plugins are safely excluded. Note that a restart of Xournal++ is required to change the activation of a plugin.

## Installation folder

Plugins shipped with Xournal++ reside in the same folder, the `plugins` subfolder of the
[shared recources folder](../file-locations.md).

In the latest development version, custom plugins can be stored in the `plugins` subfolder
of the [config folder](../file-locations.md). Create the `plugins` subfolder manually, if
it does not exist.

Each plugin has its files stored in a subfolder of the plugin folder and contains
at least a `plugin.ini` file and a Lua code file.

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
- the `accelerator` used to execute the plugin callback function. The format looks like `<Control>a` or `<Shift><Alt>F1`, see [GTK4 reference](https://docs.gtk.org/gtk4/func.accelerator_parse.html) for details. The accelerator can be omitted. Using accelerators without modifiers like (`<Alt>`, `<Control>`, `<Shift>`) is allowed, but will likely break the text tool.

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

For more extensive examples of plugins, you can check out the code of the plugins bundled with Xournal++ [in the repository](https://github.com/xournalpp/xournalpp/tree/master/plugins).

## Plugin API

The Lua Plugin can execute a number of Xournal++ functions to interact with Xournal++. Those are defined in the
[Plugin API](https://github.com/xournalpp/xournalpp/blob/7b6d84956d6bbe8615b2123c64dd0cac80afb81a/src/core/plugin/luapi_application.h#L1723-L1750).

Currently the list contains the following functions:

- `app.msgbox` displays a message box with the specified buttons and returns the button clicked by the user
- `app.glib_rename` renames a file in the file system using glib's rename function
- `app.saveAs` opens a "save as" dialog and returns the chosen file path by the user (doesn't actually save anything)
- `app.registerUi` registers menu items for the plugin (used in the `initUi`-function)
- `app.uiAction` simulates a toolbar/menubar click starting some action
- `app.uiActionSelected` notifies action listeners about selected options
- `app.sidebarAction` executes actions accessible in the sidebar
- `app.layerAction` executes actions accessible in the layer controller
- `app.changeToolColor` changes the color of any tool with color capabilities
- `app.changeCurrentPageBackground` changes the background [type](https://github.com/xournalpp/xournalpp/blob/9d1277dee22bb095c2db047bb04f89cc837aee3c/src/control/pagetype/PageTypeHandler.cpp#L98-L133) and [config](https://github.com/xournalpp/xournalpp/issues/2137#issuecomment-799956788) of the current page
- `app.changeBackgroundPdfPageNr` changes the page number of the background PDF of the current page
- [`app.getToolInfo`](https://github.com/xournalpp/xournalpp/commit/eb3b7eb292e51e2e5adb2741cbba669eb02a199b) returns all properties of a specific or the active tool **(only available in [nightly release][nightly-release] as of v1.1.3)**
- `app.getDocumentStructure` returns lots of useful info on the document, also used for applying operations on all/selected pages
- `app.scrollToPage` scrolls relatively or absolutely to a page
- `app.scrollToPos` scrolls relatively or absolutely to a new position on the same page
- `app.setCurrentPage` sets the given page as new current page
- `app.setPageSize` sets the width and height of the current page
- `app.setCurrentLayer` sets the given layer as the new current layer, and updates visibility if specified
- `app.setLayerVisibility` sets the visibility of the current layer
- `app.setCurrentLayerName` sets the name of the current layer
- `app.setBackgroundName` sets the name of the background layer
- `app.scaleTextElements` scales all text elements of the current layer by the given scale factor
- `app.getDisplayDpi` returns the configured display DPI
- `app.export` exports the current document in pdf, svg or png format
**(only available in [nightly release][nightly-release] as of v1.1.3)**
- `app.addStrokes` draws strokes on the canvas given a set of coordinates
**(only available in [nightly release][nightly-release] as of v1.1.3)**
- `app.addSplines` draws strokes on the canvas given a set of splines. The function rasterizes it, then uses the resulting series of coordinates to place the stroke on the canvas
**(only available in [nightly release][nightly-release] as of v1.1.3)**
- `app.getFilePath` opens a "Open File" dialogue and returns the chosen file path by the user
**(only available in [nightly release][nightly-release] as of v1.1.3)**
- `app.refreshPage` notifies Xournal++ of changes done by the `addStrokes` and `addSplines` functions, causing the strokes to appear on the canvas.
**(only available in [nightly release][nightly-release] as of v1.1.3)**

All those functions are documented in the same file [`luapi_application.h`](https://github.com/xournalpp/xournalpp/blob/7b6d84956d6bbe8615b2123c64dd0cac80afb81a/src/core/plugin/luapi_application.h), including example usage. Future progress on the Plugin API will be reported here. Help is always welcome.

### Using plugins to define shortcuts for ui actions

Currently Xournal++ does not have shortcuts/keybindings configurable in the preferences. However you can write your custom plugin to achieve exactly that.

The function `app.uiAction` used for simulating a toolbar/menubar click can be used for lots of different actions.
This command accepts a Lua table with keys
`"action"`, `"group"` and `"enabled"`
as its argument. The `"group"` key is only used for displaying warnings, so you can omit it. The `"enabled"` key is set to `true` by default, so you can often omit it as well. The `"action"` key accepts
one of the action strings listed in the [`Control::actionPerformed` method](https://github.com/xournalpp/xournalpp/blob/c07654780933929a92e9187ad0dc44a80fb04cc7/src/core/control/Control.cpp#L360-L950) in the source code. Note that the list of actions will change when new functionality is added to Xournal++.

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
local docStructure = app.getDocumentStructure()
local numPages = #docStructure["pages"]
local currPage = docStructure["currentPage"]
local currLayer = docStructure["pages"][currPage]["currentLayer"]
```

You can iterate through all pages by using the lines

```lua
local docStructure = app.getDocumentStructure()
local numPages = #docStructure["pages"]
for i=1, numPages do
  -- ADD CODE TO EXECUTE FOR PAGE i
end

```

Similarly you can run through all layers of a page. In case of the current page this would read like

```lua
local docStructure = app.getDocumentStructure()
local page = docStructure["currentPage"]
local numLayers = #docStructure["pages"][page]["layers"]
for i=1, numLayers do
  -- ADD CODE TO EXECUTE FOR LAYER i
end
```

## Using Lua modules

More complex Plugins will require Lua modules for certain operations. For instance if your Plugin needs
a more sophisticated GUI or wants to repeat tasks in predefined time intervals, you may want to use the
`lgi`-module via ```require("lgi")```.

The Lua package path by default contains the root folder of the plugin and the system Lua package path.
In case you need other folders in the package path, use the package.path key to add them.

[nightly-release]: https://github.com/xournalpp/xournalpp/releases/tag/nightly)
