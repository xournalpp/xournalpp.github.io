# File Format

This page outlines the main file formats used by Xournal++. The primary file
format is `.xopp`, with some plans to switch to more advanced file formats in
the near future.

## xopp

The `.xopp` file format consists of a GZIP-compressed XML file. To inspect the
XML contents, run a decompression command such as `gzip -d my_file.xopp` or
`zcat my_file.xopp`. Structurally, an `.xopp` file is like an extended version
of the `.xoj` file format used by the [Xournal program][xournal]; we briefly
explain our extensions and changes in this section.

(TODO: add text explaining the differences)

## xopz

!!! warning "Experimental Feature"

    This is an experimental feature that is only available in unstable
    development branches and is subject to change.

The `.xopz` file format is the next generation file format to be used by
Xournal++. A `.xopz` file is a zip file containing an "annotation" XML file that
stores the main journal data, along with other resources such as PDF files,
images, and audio. The XML file is the same as the one used in an `.xopp` file.
This new file format is being developed to overcome limitations and shortcomings
in the `.xopp` file format, including excessive file sizes and lack of support
for more powerful features.

The contents of the zip file are as follows:

* `contents.xml`: the main annotation data stored in XML form; this is the same
  format used in `.xopp`.
* `META-INF/version`: FIXME: legacy code (not sure why this exists)
* `background.pdf`: the background PDF used, if it exists.
* `thumbnail.jpg`: a thumbnail of the document used for preview purposes.
* `images/`: a folder containing images inserted into the document.
* `latex/`: a folder containing rendered LaTeX images

## xoj support in Xournal++

Xournal++ supports limited export to the `.xoj` format supported by Xournal.
However, there _will_ be limitations because the feature set of Xournal++ is
much larger than that of Xournal.

[xournal]: http://xournal.sourceforge.net/manual.html
