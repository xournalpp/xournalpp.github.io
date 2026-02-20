# Toolbar Colors

Xournal++ has basic support for changing the color palette used for the pen and
highlighter tools via a configuration file. GUI support for palette
customization will be implemented in the future.

Two methods for palette customization are currently available, as explained
below.

## Toolbar Color Tool Customization

In this method, the color palette is set up by manually editing the Color Tools
in in your toolbar configuration.

1. In Xournal++, make sure you are using a custom toolbar configuration. If you
   aren't, you can create a new toolbar configuration using the menu item
   `Edit > Toolbars > Manage`.
2. Using a text editor, open the `toolbar.ini` file contained in the Xournal++
   config folder. See [File locations](../file-locations.md) for the location of
   this folder on your operating system.
3. Find the section corresponding to your toolbar configuration, e.g.
   `[My Toolbar]`.
4. Each line under this section header defines the tools used in each toolbar.
   Find the `COLOR(0x??????)` items on each line. The six question marks
   correspond to a color in RGB hexadecimal format. Replace these hexadecimal
   numbers with your desired colors. To find the right numbers, you can use an
   online hex RGB color picker tool such as [this one][mdn color picker].

## Toolbar Palette Files

In this method, the color palette is set up by editing a GIMP color palette
file.

The palette will be loaded from files with `.gpl` extension (e.g. `palette_name.gpl`)
saved in the `palettes` folder within the [Xournal++ config folder](../file-locations.md).
You will need to manually create a `.gpl` file for each custom palette. 
The easiest way to get started is to adjust the default color palette template (scroll down to find it).

1. For each palette you want to create, place the `palette_name.gpl` file in the `palettes` folder
inside [Xournal++ config folder](../file-locations.md).
2. Restart Xournal++.
3. Open `Edit -> Preferences -> Palette` to switch to the new palette.

Note: If you are using a version older than v1.3.0, save `palette.gpl` in the
[config folder](../file-locations.md) instead.

### .gpl File Format

!!! note

    The `.gpl` file format is not authoritatively defined anywhere, so the file
    format described below may be specific to Xournal++. However, Xournal++
    tries to be compatible with `.gpl` files used with other software such as
    GIMP. If you find a `.gpl` file that works in other software but does _not_
    work with Xournal++, [please file a bug report](https://github.com/xournalpp/xournalpp/issues).

As an example, the default color palette of Xournal++ is shown below.

```
GIMP Palette
Name: Xournal Default Palette
#
0 0 0 Black
0 128 0 Green
0 192 255 Light Blue
0 255 0 Light Green
51 51 204 Blue
128 128 128 Gray
255 0 0 Red
255 0 255 Magenta
255 128 0 Orange
255 255 0 Yellow
255 255 255 White
```

The palette file consists of several parts:

 1. **Header**: every palette file must begin with the line `GIMP Palette`,
    otherwise the file will not be a valid `.gpl` file.
 2. A list of **attributes** of the form `Key: Value`, one per line. These
    attributes are metadata that describe the palette.
 3. Lines beginning with `#` are **comments**, which are ignored by the file
    parser. The comment used above is to distinguish the attributes from the
    colors of the palette.
 4. The **colors** of the palette, one per line, in the format `RRR GGG BBB Name`.
    The `RRR`, `GGG`, and `BBB` correspond to the RGB format of the color,
    specified as base-10 integers in the range `0-255`. To find the right
    numbers, you can use an online RGB color picker tool such as [this one][mdn
    color picker].

!!! note

    It's recommended to have at least 11 colors in a palette, as the default
    toolbar has 11 Color Items. If your palette has fewer colors, a warning
    will be displayed in the console, and the extra Color Items will cycle
    through the palette.

If Xournal++ cannot parse the palette file (i.e., the palette file is invalid),
it will load the default palette. If this happens, there are two ways to get
your palette file to load.

**Option 1: Debugging**: run `xournalpp` from the command line and check for an
error message explaining why the palette file is invalid. Then, fix your
`palette.gpl` file, restart Xournal++, and check if the palette loaded
correctly. If not, repeat this debugging step.

**Option 2: Fresh Start**: delete `palette.gpl`, restart Xournal++ to create
a new default `palette.gpl` file, and edit again.

### Palette Resources/Tips

#### Creating your own palette

 - Find RGB values to use in palettes with the [MDN color picker][mdn color
   picker]
 - Use a palette editor such as [Gpick](http://www.gpick.org/) to create a `.gpl`
   file

#### Reusing existing palettes

 - "The [Lospec Palette List](https://lospec.com/palette-list) is a database of
   palettes for pixel art" (directly quoted from their website). Palettes can be
   exported to `.gpl` format.
 - You can reuse `.gpl` files from other software compatible with `.gpl`
   palettes, such as Krita, Inkscape, or GIMP. For example, Linux users may be
   able to find existing palettes in locations such as
   `/usr/share/gimp/2.0/palettes` or `/usr/share/krita/palettes`.

[mdn color picker]: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool
