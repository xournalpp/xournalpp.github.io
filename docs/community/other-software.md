# Relation to other software

This section is about the relation between Xournal++ and other open source software products, which either share a decent amount of similarity and compatibility or which can be combined
nicely with Xournal++.

## Xournal

Xournal++ started as a C++ rewrite of Xournal by [Denis Aroux](http://people.math.harvard.edu/~auroux/), which is programmed in C and hosted on sourceforge.
Xournal++ is actively developed, while Xournal has stopped developing new features after mid 2016. Denis Aroux notes on the [Xournal website](http://xournal.sourceforge.net/):

> You may also want to try out Xournal++ (which started out as a rewrite of Xournal in C++, but now has evolved well beyond the original, while retaining a decent amount of compatibility).

Xournal++ still uses some parts of Xournal's code, most notably Xournal's shape recogntion code. The two applications share a similar look. Xournal++ contains most of Xournal's functionality,
while adding some useful pluses.
Xournal++ can open Xournal .xoj-documents and export to it in compatibility mode. We are greatly thankful to Denis Aroux for his wonderful software and all of Xournal's contributors.

The following lists highlight the differences between the latest development version Xournal++ {{ version.latest_unstable }} and Xournal 0.4.8.2016.

### Features available in Xournal++, but not in Xournal

- LaTeX tool
- Audio recording and playback
- Lua plugins
- Pen pressure support
- Sidebar with page and layer previews
- Page layout in multiple rows/columns
- Grid and rotation snapping
- Select object tool
- Rectangle, Circle, Arrow, Coordinate system and Spline drawing types
- Flexible remapping of input devices
- Zoom gestures
- Drawing modifiers by drawing direction
- Export to .png and .svg, and various export options
- Periodic autosave and auto-backup tool
- Staves and Isodotted page backgrounds
- More cursor icon options
- Floating toolbox
- Configurable toolbars
- Language selectable in the GUI
- Option to easily append new pdf pages
- More distribution options on Linux (PPA, flatpak, appimage and snap packages)
- Translations in more languages

### Features available in Xournal, but not in Xournal++

- Input via Xinput (which gives better strokes on some devices)
- One page mode (useful in presentations)
- A complete [documentation](http://xournal.sourceforge.net/manual.html) and a [well documented file format](http://xournal.sourceforge.net/manual.html#file-format)

### Known issues/bugs/inconveniences of Xournal, resolved in Xournal++

TODO

### Performance comparision between Xournal++ and Xournal

TODO

## Xournal++ mobile

Xournal++ lacks the option to be used on mobile devices other than Linux phones. [Xournal++ mobile](https://gitlab.com/TheOneWithTheBraid/xournalpp_mobile) tries
to fill this gap. It ports the main features of Xournal++ to various Flutter platforms like Android, iOS and the Web. It uses the same `.xopp` file format as Xournal++ does.
Xournal++ Mobile is currently still in early development. Don't expect a fully featured app, but rather a modern looking app to edit basic `.xopp`-files on the mobile phone or the Web. Strokes, images and LaTeX formulas can be rendered, PDF backgrounds not yet.

!!! note
    Currently Xournal++ mobile is unmaintained and no new features have been added since March 2021. If anyone is interested in taking over maintanance, let us know.

## Linwood Butterfly

If you are looking for a maintained and great looking open source note-taking app with mobile device support comparable to Xournal++ mobile, there is [Linwood Butterfly](https://docs.butterfly.linwood.dev/). It has recently added an importer for Xournal++'s `.xopp`-files and is working on an exporter, too, according to the developer of this app. Like Xournal++ mobile, the app is Flutter-based and available for Android, Windows, Linux, and in the Web. So Linwood Butterfly is to be tried if you want to work with `.xopp`-files on a mobile device/on the web or if you simply prefer a more minimalistic app.

## Rnote

Xournal++ is still working on its port to Gtk 4. Meanwhile [Rnote](https://rnote.flxzt.net/) is already built from scratch for Gtk 4. Look no further if you are seeking for a modern looking and featureful Gnome/Libadwaita based app with mostly the same purpose as Xournal++, but centered around an infinity canvas instead of page-based view. Rnote uses its own file format, yet offers import from and export to Xournal++'s `.xopp`-format. 

## Mr Writer

While Xournal++ and Xournal are based on GTK+ 3 and GTK+ 2, respecitively, [Mr Writer](https://unruhschuh.github.io/MrWriter/) is a QT-based App which shares a lot of functionality with Xournal and Xournal++.
In the author's words:
>MrWriter is an application aiming to replace both pen and paper for handwritten note taking, as well as blackboards for giving lectures in front of students. It is highly inspired by Xournal / Xournal++ the focus is more on taking notes and platform independence, rather than PDF annotation. Xournal files (.xoj) can be imported, but only strokes get recognized.

Mr Writer has its own file format, called `.moj` which Xournal++ is capable of opening directly. Moreover since Xournal++ can export to`.xoj`-files you also can basically also open files created by Xournal++ in Mr Writer.

## Joplin

If you are looking for a text based note taking app with great organizational tools, you may want to try out [Joplin](https://joplinapp.org/). While Xournal++ excells in handwriting and PDF annotation, Joplin can organise your notes into notebooks in a nice tree structure and synchronize them via Cloud services like Nextcloud, Dropbox, OneDrive and WebDAV. You can attach all kind of files to a Joplin file, including Xournal++ `.xopp`-files. Xournal++ and Joplin complement each other pretty well, if you take handwritten notes in class (or elsewhere) and want to keep them nicely organized and synchronized.


## OBS Studio

For creating video recordings or live streams of lectures that you present using Xournal++ we recommend to use [OBS Studio](https://obsproject.com/). This free and open source tool is available on all major platforms.
