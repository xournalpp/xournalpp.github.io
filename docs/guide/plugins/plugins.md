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

### Error-handling

Functions of the xounalpp Lua-Api will return Lua errors which can be handled by
calling the function with
[`pcall`](https://www.lua.org/manual/5.4/manual.html#pdf-pcall) when something
_unexpected happens_ (like wrong arguments passed). In rare cases
`nil, errorMessage` might be returned to silently throwing an error. This is
reserved for _expected things_ (like the resource is unavailable). You may make
such errors to Lua errors by wrapping with [`assert`](https://www.lua.org/manual/5.4/manual.html#pdf-assert).

### Functions

Any Lua Plugin can execute a number of Xournal++ functions to interact with Xournal++.Those are defined in the Plugin API as seen in the
[definition file](https://github.com/xournalpp/xournalpp/blob/master/plugins/luapi_application.def.lua). That file shows the list of all Xournal++ functions, its function parameters, return values and example usage. Moreover it can be used with the [Lua language server](https://luals.github.io/) to get code completion, hover tooltips, jump-to-definition, find-references, and more. For writing plugins using
one of the many [code editors](https://microsoft.github.io/language-server-protocol/implementors/tools/) that support the Lua language server is advisable. If you need
more information how these Xournal++ functions are defined, see the
`luapi_application.h` file which is relevant to your version of xournalpp:

* [1.1.x series](https://github.com/xournalpp/xournalpp/blob/release-1.1/src/plugin/luapi_application.h)
* [1.2.x series](https://github.com/xournalpp/xournalpp/blob/release-1.2/src/core/plugin/luapi_application.h)
* [nightly builds](https://github.com/xournalpp/xournalpp/blob/master/src/core/plugin/luapi_application.h)

### Using plugins to define shortcuts for ui actions

Currently Xournal++ does not have shortcuts/keybindings configurable in the preferences. However you can write your custom plugin to achieve exactly that.

The function `app.uiAction` used for simulating a toolbar/menubar click can be used for lots of different actions.
This command accepts a Lua table with keys
`"action"` and `"enabled"` as its argument. The `"enabled"` key is set to `true` by default, so you can often omit it. The `"action"` key accepts
one of the action strings listed in the source file [ActionBackwardCompatibilityLayer.cpp](https://github.com/xournalpp/xournalpp/blob/master/src/core/plugin/ActionBackwardCompatibilityLayer.cpp). Note that the list of actions will change when new functionality is added to Xournal++.

For example use:

```lua
app.uiAction({ action = "ACTION_RULER" })
```

to activate the ruler (for drawing line segments) or

```lua
app.uiAction({ action = "ACTION_TOOL_FILL", enabled = false })
```

to turn off filling of shapes.

### Retrieving information about the document and iterating through pages and layers

The `app.getDocumentStructure` function yields a Lua table of the following shape:

```lua
{
  pages = {
    {
      pageWidth = number,
      pageHeight = number,
      isAnnoated = bool,
      pageTypeFormat = string,
      pdfBackgroundPageNo = integer (0, if there is no pdf background page),
      layers = {
        [0] = {
          isVisible = bool
        },
        [1] = {
          isVisible = bool,
          isAnnotated = bool
        },
        ...
      },
      currentLayer = integer
    },
  ...
  }
  currentPage = integer,
  pdfBackgroundFilename = string (empty if there is none)
}
```

So for example to get the number of all pages, the page number of the current page and the layer ID of the current layer use the code:

```lua
local docStructure = app.getDocumentStructure()
local numPages = #docStructure.pages
local currPage = docStructure.currentPage
local currLayer = docStructure.pages[currPage].currentLayer
```

You can iterate through all pages by using the lines

```lua
local docStructure = app.getDocumentStructure()
local numPages = #docStructure.pages
for i=1, numPages do
  -- ADD CODE TO EXECUTE FOR PAGE i
end

```

Similarly you can run through all layers of a page. In case of the current page this would read like

```lua
local docStructure = app.getDocumentStructure()
local page = docStructure.currentPage
local numLayers = #docStructure.pages[page].layers
for i=1, numLayers do
  -- ADD CODE TO EXECUTE FOR LAYER i
end
```

## Using Lua modules

More complex Plugins will require Lua modules for certain operations. For instance if your Plugin needs
a more sophisticated GUI or wants to repeat tasks in predefined time intervals, you may want to use the
`lgi`-module via `require("lgi")`.

The Lua package path by default contains the root folder of the plugin and the system Lua package path.
In case you need other folders in the package path, use the package.path key to add them.

[nightly-release]: https://github.com/xournalpp/xournalpp/releases/tag/nightly)
