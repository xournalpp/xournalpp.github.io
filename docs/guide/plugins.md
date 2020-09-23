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
- the `accelerator` used to execute the plugin callback function. The format looks like `<Control>a` or `<Shift><Alt>F1` or `<Release>z` (for key release). See [GTK3 reference](https://developer.gnome.org/gtk3/stable/gtk3-Keyboard-Accelerators.html#gtk-accelerator-parse) for details. The accelerator can be omitted. Using accelerators without (`<Alt>`, `<Control>`, `<Shift>`) modifiers is allowed, but will likely break the text tool.

You can register multiple menu entires/accelators in the same plugin by using multiple `app.registerUi`. 

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

The Lua Plugin can execute a (small) number of Xournal++ functions to interact with Xournal++. Those are defined and documented in the 
[Plugin API](https://github.com/xournalpp/xournalpp/blob/master/src/plugin/luapi_application.h#311-317?).

Currently the list contains the following functions:

- `app.msgbox` for displaying messages to the user and letting the user choose an option by clicking a button
- `app.registerUi` used in the `initUi`-function
- `app.uiAction` for simulating a toolbar/menubar click starting some action,
- `app.uiActionSelected` for notifying action listeners about selected options,
- `app.changeCurrentPageBackground` for changing the background of the current page,
- `app.changeToolColor` for changing the color of any tool with color capabilities,
- `app.saveAs` for retrieving the filename from a native saveAs dialog.

Two more functions are currently been added to the API in a [Pull Request for handwriting recognition](https://github.com/xournalpp/xournalpp/pull/2176). 

- `app.getStrokes` gets the strokes from the selection tool or a page layer
- `app.getWidthAndHeight` gets the width and the height from the selection tool or a page layer

Future progress on the Plugin API will be reported here. Help is always welcome.

### Using plugins to define shortcuts for ui actions

Currently Xournal++ does not have shortcuts/keybindings configurable in the preferences. However you can write your custom plugin to achieve exactly that.

The function `app.uiAction` used for simulating a toolbar/menubar click can be used for lots of different actions. 
This command accepts a Lua table with keys
`"action"`, `"group"` and `"enabled"`
as its argument. The `"group"` key is only used for displaying warnings, so you can omit it. The `"enabled"` key is set to `true` by default, so you can often omit it as well. The `"action"` key accepts
one of the following values:

- `"ACTION_NEW", "ACTION_OPEN", "ACTION_ANNOTATE_PDF", "ACTION_SAVE", "ACTION_SAVE_AS", "ACTION_EXPORT_AS_PDF", "ACTION_EXPORT_AS", "ACTION_PRINT", "ACTION_QUIT"` for **file menu** actions
- `"ACTION_UNDO", "ACTION_REDO", "ACTION_CUT", "ACTION_PASTE", "ACTION_DELETE", "ACTION_SETTINGS"` for **edit menu** actions
- `"ACTION_GOTO_FIRST", "ACTION_GOTO_BACK", "ACTION_GOTO_PAGE", "ACTION_GOTO_NEXT", "ACTION_GOTO_LAST", ACTION_GOTO_NEXT_ANNOTATED_PAGE", "ACTION_GOTO_PREVIOUS_ANNOTATED_PAGE"` for **navigation menu** actions
- `"ACTION_NEW_PAGE_BEFORE", "ACTION_NEW_PAGE_AFTER", "ACTION_NEW_PAGE_AT_END", "ACTION_DELETE_PAGE", "ACTION_PAPER_FORMAT", "ACTION_CONFIGURE_PAGE_TEMPLATE", "ACTION_PAPER_BACKGROUND_COLOR"` for **journal menu** actions
- `"ACTION_TOOL_PEN", "ACTION_TOOL_ERASER", "ACTION_TOOL_ERASER_STANDARD", "ACTION_TOOL_ERASER_DELETE_STROKE", "ACTION_TOOL_ERASER_WHITEOUT", "ACTION_TOOL_HILIGHTER", "ACTION_TOOL_TEXT", "ACTION_TOOL_IMAGE", "ACTION_TOOL_SELECT_RECT", "ACTION_TOOL_SELECT_REGION", "ACTION_TOOL_SELECT_OBJECT", "ACTION_TOOL_PLAY, OBJECT", "ACTION_TOOL_VERTICAL_SPACE", "ACTION_TOOL_HAND", "ACTION_TOOL_FLOATING_TOOLBOX", "ACTION_TOOL_DRAW_RECT", "ACTION_TOOL_DRAW_CIRCLE", "ACTION_TOOL_DRAW_ARROW", "ACTION_TOOL_DRAW_COORDINATE_SYSTEM", "ACTION_RULER", "ACTION_TOOL_DRAW_SPLINE", "ACTION_SHAPE_RECOGNIZER", "ACTION_TOOL_DEFAULT", "ACTION_TOOL_FILL", "ACTION_SIZE_VERY_FINE", "ACTION_SIZE_FINE", "ACTION_SIZE_MEDIUM", "ACTION_SIZE_THICK", "ACTION_SIZE_VERY_THICK", "ACTION_TOOL_LINE_STYLE_PLAIN", "ACTION_TOOL_LINE_STYLE_DASH", "ACTION_TOOL_LINE_STYLE_DASH_DOT", "ACTION_TOOL_LINE_STYLE_DOT", "ACTION_TOOL_ERASER_SIZE_VERY_FINE", "ACTION_TOOL_ERASER_SIZE_FINE", "ACTION_TOOL_ERASER_SIZE_MEDIUM", "ACTION_TOOL_ERASER_SIZE_THICK", "ACTION_TOOL_ERASER_SIZE_VERY_THICK", "ACTION_TOOL_PEN_SIZE_VERY_FINE", "ACTION_TOOL_PEN_SIZE_FINE", "ACTION_TOOL_PEN_SIZE_MEDIUM", "ACTION_TOOL_PEN_SIZE_THICK", "ACTION_TOOL_PEN_SIZE_VERY_THICK", "ACTION_TOOL_PEN_FILL", "ACTION_TOOL_PEN_FILL_TRANSPARENCY", "ACTION_TOOL_HILIGHTER_SIZE_VERY_FINE", "ACTION_TOOL_HILIGHTER_SIZE_FINE", "ACTION_TOOL_HILIGHTER_SIZE_MEDIUM", "ACTION_TOOL_SIZE_THICK", "ACTION_TOOL_HILIGHTER_SIZE_VERY_THICK", "ACTION_TOOL_HILIGHTER_FILL", "ACTION_TOOL_HILIGHTER_FILL_TRANSPARENCY", "ACTION_SELECT_FONT", "ACTION_TEX"` for **tools menu** actions
- `"ACTION_ZOOM_100", "ACTION_ZOOM_FIT", "ACTION_ZOOM_IN", ACTION_ZOOM_OUT", "ACTION_VIEW_PAIRED_PAGES", "ACTION_VIEW__PRESENTATION_MODE", "ACTIoN_MANAGE_TOOLBAR", "ACTION_CUSTOMIZE_TOOLBAR", "ACTION_FULLSCREEN", "ACTION_SET_COLUMNS_1", ... , "ACTION_SET_COLUMNS_8", "ACTION_SET_ROWS_1", ... , "ACTION_SET_ROWS_8", "ACTION_SET_LAYOUT_HORIZONTAL", "ACTION_SET_LAYOUT_VERTICAL", "ACTION_SET_LAYOUT_L2R", "ACTION_SET_LAYOUT_R2L", "ACTION_SET_LAYOUT_T2B", "ACTION_SET_LAYOUT_B2T", "ACTION_AUDIO_RECORD", "ACTION_AUDIO_PAUSE_PLAYBACK", "ACTION_AUDIO_SEEK_FORWARDS", "ACTION_ACUDIO_STOP_PLAYBACK", "ACTION_ROTATION_SNAPPING", "ACTION_GRID_SNAPPING"` for **view menu** actions
- `"ACTION_PLUGIN_MANAGER"` for **plugin menu** actions
- `"ACTION_HELP", "ACTION_ABOUT"` for **help menu** actions

For example use:

```lua
app.uiAction({["action"]="ACTION_RULER"})
```

to activate the ruler (for drawing line segments) or

```lua
app.uiAction({["action"]="ACTION_TOOL_FILL", ["enabled"]=false})
```

to turn of filling of shapes.

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
- the `ColorCycle`Plugin lets you cycle through a list of colors for the current tool by using the same accelerator repeatedly
- The `HandwritingRecognition` Plugin (work in progress) uses the google cloud-based IME handwriting API to recognize handwritten text from a selection or page layer in a user-specified language.

