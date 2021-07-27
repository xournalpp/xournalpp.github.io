# Tips

## GNOME Files/Nautilus: Convert notes to PDF from context menu

To be able to select and convert Xournal++ files to PDF from the context menu in Nautilus (GNOME Files),
one can save [this script](xopp-to-pdf) as
`$HOME/.local/share/nautilus/scripts/xopp-to-pdf` and make it executable.

![screenshot-of-Nautilus-context-menu-with-action-to-convert-xopp-files-to-pdf](xopp-to-pdf_context-menu.png)

If `libnotify` is installed, one will get a notification once the conversion is done.
