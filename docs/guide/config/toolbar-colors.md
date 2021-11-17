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

1. Using a text editor, open or create the `palette.gpl` file contained in the
   Xournal++ config folder. See [File locations](../file-locations.md) for the
   location of this folder on your operating system.
2. TODO: explanation of the palette.gpl syntax
3. TODO: explanation of how to add a color (mention the color picker tool also)

An example `palette.gpl` file is shown below ([source](https://github.com/xournalpp/xournalpp/issues/1812#issuecomment-723679463)):

```
GIMP Palette
Name: Xournal New Palette.gpl
#
255 225 107 #FFE16B
255 161  84 #FFA154
205 158 247 #CD9EF7
155 219  77 #9BDB4D
100 186 255 #64BAFF
128 128 128 #808080
 58 145   4 #3A9104
237  83  83 #ED5353
  0  46 153 #002E99
  0   0   0 #000000
255 255 255 #FFFFFF
```

[mdn color picker]: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool
