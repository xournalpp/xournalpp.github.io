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
   `View > Toolbars > Manage`.
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

!!! note

    This feature is only available on Xournal++ nightly builds.

In this method, the color palette is set up by editing a GIMP color palette
file.

The easiest way to get started with this is to let Xournal++ create the default palette file for you.
You can then use this as a template to adjust it to your needs.

Prerequisite: Xournal++ ran at least once with the new version

 1. Open `palette.gpl` in the [config file location](../file-locations.md)
 2. Edit the `palette.gpl` to your needs
 3. Restart Xournal++

### .gpl File Format

!!! note

    The `.gpl` file format is not authoritatively defined anywhere.
    Hence the below definition might only be valid for Xournal++.
    However, we are trying to be compatible with `.gpl` files as used in other Software.
    In case you find a case where the `.gpl` file is not parsable by Xournal++ but you think it should be parsable since for example GIMP accepts it, please file a bug report.

Lets start with an example:

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

This is the default color palette of Xournal++, which is created if no palette is found.

It consists of several Parts:

 1. Header: `GIMP Palette` any file not having exactly this string at the first line will not be accepted as `.gpl` file
 2. A list of attributes separated by `:`.
 3. An optional comment line as separator.
 4. The colors of the palette as space separated `RGB` values together with a name

The parser checks each line apart from the first line in the following order:

 1. Can line be parsed as **comment** (i.e. first character is `#`)
 2. Can line be parsed as **attribute** (i.e. two string separated by `:`)
 3. Can line be parsed as **color** (i.e. `RRR GGG BBB Name`)
 4. Otherwise abort parsing

In case Xournal++ cannot parse the palette file (i.e. it cannot parse a line), it loads the default palette.
If this happens there are two ways to get your palette file to load.

Option 1, Debugging:

 - run `xournalpp` from command line 
 - check the error message (it tells you which line was not parsable)
 - fix line in your `palette.gpl`
 - retry

Option 2, Fresh Start:

 - remove the `palette.gpl` file
 - start `xournalpp` (this will create a new default `palette.gpl` file)
 - adjust `palett.gpl` to your needs

!!! note
    
    It's recommended to have at least 11 colors in your palette as the default toolbar has 11 ColorItems.
    In case your palette has less, Xournal++ will show a warning in the CLI and just cycle through the palette.

### Palette Resources/Tips

#### Creating your own palette

 - [MDN color picker](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool)
 - [Gpick](http://www.gpick.org/)

#### Getting complete palettes

 - [lospec](https://lospec.com/palette-list)
 - `locate '.gpl'` on your machine in case you have krita, inkscape, or GIMP installed
      - e.g. `/usr/share/gimp/2.0/palettes/`
      - e.g. `/usr/share/inkscape/palettes/`
      - e.g. `/usr/share/krita/palettes/`
