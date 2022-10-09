# Working With PDF Files

Xournal++ supports various features for annotating on top of PDF files.

The main way to interact with an external PDF file is to use the PDF file as the
background of a journal.

## Setting a PDF file as a background

To create a new journal that uses a PDF file as a background, you can use the
menu option `File > Annotate PDF` or `File > Open`. This will open a dialog that
will allow you to select a PDF file, and then it will create a new journal with
that PDF file as the background.

!!! note
    Xournal++ currently stores the journal file (`.xopp`) separately from the
    PDF file. When you save a journal file, the _absolute path_ of the PDF file
    will be stored in the `.xopp` file. This means that if you move the `.xopp`
    file to another computer, or if you move the PDF to another location,
    Xournal++ will not be able to find your background PDF. When this happens,
    opening the journal file will lead to Xournal++ prompting you to either
    identify the new location of your PDF or select a new one.
    <br/>
    <br/>
    To work around this problem, you can use the [PDF attach mode](#attach-mode)
    as described below.
    <br/>
    <br/>
    There are future plans to introduce a "bundled" file format that stores the
    journal and the PDF file in the same file. For more information, see
    [this issue on our issue tracker](https://github.com/xournalpp/xournalpp/issues/937).

### Attach mode

If you use `File > Annotate PDF` to create a new journal, you can check the
`Attach file to the journal` checkbox to enable "attach mode". When attach mode
is enabled for a journal, the PDF file will always be copied to the same
directory as the `.xopp` file when saving, even if the `.xopp` file is moved.
Futhermore, the journal file will store a _relative path_ to the PDF file.

Together, this means that you can savely "move" a `.xopp` file that has a PDF
background _as long as you ensure that you "move" the file using `File > Save
As`_!

!!! bug
    In Xournal++ 1.1.1 and older, there was a bug where attach mode settings
        would not be remembered when loading. This bug has been fixed in Xournal++
    1.1.2.

## Navigating the PDF file

If the PDF file contains a table of contents, the "Outline" tab of the sidebar
will display the table of contents. Clicking on an entry in the "Outline" tab
will jump the canvas to the corresponding page.

## Relationship between the Journal and the PDF background

Due to the way Xournal++ works, there are several limitations on modifying
journal pages or modifying the background PDF file:

* Because Xournal++ treats the background PDF file separately, changing the
  background PDF file may cause annotations to "go out of sync" with the
  background PDF. For example, if pages are removed from the background PDF,
  then the journal file will still contain pages referencing the removed pages.
  Xournal++ will not delete the annotations on those pages, but the (removed)
  pages will no longer be rendered.
* If pages are added to the background PDF file, Xournal++ will _not_
  automatically insert the newly added pages. The new pages must be inserted
  into the journal using the `Journal > Append New PDF Pages` menu option.

## Searching for PDF Text

To search for text contained in a PDF background page, use `Edit > Search` or
the keyboard shortcut <kbd>Ctrl</kbd><kbd>F</kbd>. This will open a prompt that
will allow you to search for the given text on all PDF pages.

## Interacting with PDF Pages

!!! note
    This feature is only available in the nightly version.

The PDF Toolbox feature can be used to interact with the background PDF pages.
This feature is available through the following tools:

* Select Linear PDF Text: select lines of text on the PDF
* Select PDF Text in Rectangle: select text on the PDF using a rectangular
  cursor

For more information, see the [PDF Tools](tools/pdf_tools.md) page.

## Exporting to PDF

The journal file and its PDF background can be exported in the usual way using
the `File > Export as PDF` menu option.

Due to the way that Xournal++ deals with PDF files, there are several
limitations on the export:

* Once you export annotations to PDF format, the annotations in the PDF file
  cannot be edited. This is because the PDF format is not designed to be edited.
* Xournal++'s PDF export does not preserve annotations that are built-in to the
  PDF file, such as pop-up notes and forms.
* Xournal++ will not allow you to override the background PDF when you export.
  This is because overriding the background PDF will cause the annotations in
  the journal to become inconsistent with the actual contents of the (newly
  overridden) background PDF. For a more detailed discussion of this problem,
  see [this issue](https://github.com/xournalpp/xournalpp/issues/2363).
