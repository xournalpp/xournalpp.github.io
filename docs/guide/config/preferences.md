# Configuration

# Preferences
Xournal ++ has multiple options that can be configured and customized. Most of these features can be found under **Edit > Preferences**.

## Load / Save

### Autosaving

Enable or disable automatic saving and set the time interval in which it will be done. If the document was previously saved in any folder, the autosave document will be in the same location as a hidden file. Otherwise the file will be saved in **$XDG_CONFIG_HOME/xournalpp/autosave** or if XDG_CONFIG_HOME is not set in **~/.config/xournalpp/autosave**. TODO: Windows

!!! note

    The autosave path is about to change in release 1.2.0 and has already been changed in Xournal++ nightly builds.<br>
    Linux: **$XDG_CACHE_HOME/xournalpp/autosaves** or if XDG_CACHE_HOME is not set **~/.cache/xournalpp/autosaves**.<br>
    Windows: TODO. See the documentation for [FOLDERID_InternetCache](https://docs.microsoft.com/en-us/windows/win32/shell/knownfolderid#FOLDERID_InternetCache).

### Default Save Name

Name that will be proposed by default when using **Save As** option. Allows the use of placeholders.

### Autoloading Journals

TODO

## Input System

TODO

## Mouse

In this section you can set the behavior of the **middle and right mouse buttons** to associate tools with it. Each tool allows sub settings for thickness, color, stroke type, etc. if they are available.

## Stylus

### Pressure Sensitivity

Enables / disables pressure sensitivity to make thicker strokes when pressing the stylus more heavily. Only effective on tablets that support this feature.

### Artifact Workaround

TODO

### Stylus Buttons

Specifies the behavior of the buttons on the stylus when pressed, allowing them to be associated with tools just like the buttons on the mouse.

The **Button 1** and **Button 2** are typical side buttons. The **Eraser** is supported only by some styluses and works using the opposite side of the pen tip; precisely like a pencil from real life.

These changes are **not** persistent; in other words, once the stylus button is released, the previously held tool will be selected again.


## Touchscreen

TODO

## View

TODO

## Zoom

TODO

## Drawing Area

TODO

## Defaults

TODO

## Audio Recording 

TODO

## LaTeX

TODO

## Language

TODO
