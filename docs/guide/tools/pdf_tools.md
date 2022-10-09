# PDF Tools

!!! note
    This feature is only available in the nightly version.

The PDF tools can be used to interact with the background PDF.

## PDF Toolbox

The PDF Toolbox provides various features for interacting with PDF pages. The
toolbox is first activated using one of the tools described below, and then a
popup window will show some actions that can be taken.

### Selecting Text

There are two tools that can be used to select text on a PDF: Select Linear PDF
Text and Select PDF Text in Rectangle.

The
<span class="tool-label">**Select Linear PDF Text Tool** ![Select Linear PDF Text Tool icon](https://raw.githubusercontent.com/xournalpp/xournalpp/master/ui/iconsColor-light/hicolor/scalable/actions/xopp-select-pdf-text-ht.svg)</span>
is used to select lines of text.

* Click to start the selection, and drag the pen/mouse cursor to select text
  linearly. Release to finish the selection.
* Double tap/click to select by lines.
* Triple tap/click to select by paragraph.

The
<span class="tool-label">**Select PDF Text in Rectangle Tool** ![Select Linear PDF Text Tool icon](https://raw.githubusercontent.com/xournalpp/xournalpp/master/ui/iconsColor-light/hicolor/scalable/actions/xopp-select-pdf-text-area.svg)</span>
is similar, except that it creates a selection rectangle such that all text
contained in the rectangular region will be selected. Using double/triple
selection with this tool will default to the behavior of the linear selection
tool.

### Interacting with Selected Text

Once text selection is finalized, a popup window with several actions will be
shown.

* The large button with the copy icon will copy the selected text to the clipboard.
* The three buttons on the right side of the toolbox will create a stroke that
  (from top to bottom, respectively): 1) highlights the selected text; 2)
  underlines the selected text; 3) strikes through the selected text.
* The button at the bottom left will toggle between linear selection and
  region selection.
