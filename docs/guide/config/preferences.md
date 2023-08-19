# Configuration

# Preferences
Xournal ++ has multiple options that can be configured and customized. Most of these features can be found under **Edit > Preferences**.

## Load / Save

### Autosaving

Enable or disable automatic saving and set the time interval in which it will be done. If the document was previously saved in any folder, the autosave document will be in the same location as a hidden file. Otherwise the file will be saved in your [Config folder](../file-locations.md#config-folder) in the subfolder `autosave`.

!!! note

    The autosave path is about to change in release 1.2.0 and has already been changed in Xournal++ nightly builds.<br>
    Autosaves are now in your [Cache folder](../file-locations.md#cache-folder) in the subfolder `autosaves`.

### Default Save Name

Name that will be proposed by default when using **Save As** option. Allows the use of placeholders.

### Autoloading Journals

TODO

## Input System

The Input System tab is used to configure how to handle input devices such
as mice, styluses, keyboards, and touchscreens.

### Overriding Device Classes

By default, Xournal++ will guess the "class" of each physical input device that
is recognized by your computer.
Sometimes the guess will be wrong (e.g., if your stylus is detected as a
touchscreen), in which case you may need to manually override device class in
the `Input Devices` section.

Each device recognized by Xournal++ will be displayed in the format of `Name
(guessed device type)`, one per line.
The right side of each line will have a dropdown menu that can be used to
override the device class.

The device classes are described below:

* **Disabled**: do not handle any input from the physical device.
* **Mouse**: treat the physical device like a mouse, but do not allow keyboard
  input from the physical device.
  Supports pressure sensitivity if assigned to a stylus.
* **Mouse+Keyboard Combo**: similar to mouse, but allow keyboard input.
  This device class should be used for wireless USB "Mouse + Keyboard Combo"
  devices, such as popular ones from Logitech.
* **Pen**: a stylus device tip. Supports pressure sensitivity.
* **Eraser**: forces all input from the physical device to be used with the
  Eraser Tool.
* **Touchscreen**: a touchscreen input.
  Supports pressure sensitivity and gestures.

Note that each device class has its own tab in Preferences for additional
configuration.

### Input Options

* When the **Enable drawing outside window** option is enabled (default), moving
  the input device out of the canvas will pause points from being added to the
  stroke until the input device reenters the canvas.
  When the option is disabled, the current stroke will be finalized when the
  input device leaves the canvas.

* For some stylus devices, stylus button presses may not be detected when the
  device is hovering.
  If you think this could be a hardware and not a driver problem, one potential
  workaround is to set the **Merge button events with stylus tip events**
  setting.
  This will cause Xournal++ to simulate a stylus tip press whenever a stylus
  button is pressed.

    <!-- This weird indentation is needed for multi-paragraph list items. -->

    Note that if your device already works properly with this setting off,
    turning it on can cause issues!

    !!! note
        On Windows, you are strongly recommended to turn this setting on. The
        reason is that the Windows Ink API is designed to only report stylus
        button input when the stylus tip is pressed down, so Xournal++ won't
        interpret the button events correctly unless the setting is turned on.

        If you're using Linux with an X11 environment, you will likely need to
        enable **Merge button events with stylus tip events** if `xsetwacom get
        <id> TabletPCButton` (where you can retrieve your stylus device id with
        `xsetwacom --list devices`) reports that
        [`TabletPCButton`](https://www.mankier.com/1/xsetwacom#Parameters-TabletPCButton)
        is on.

        The information in this note is summarized from these comment threads on
        GitHub:

        * [#2316 (comment by rolandlo)](https://github.com/xournalpp/xournalpp/issues/2316#issuecomment-860083264)
        * [#2316 (comment by lb90)](https://github.com/xournalpp/xournalpp/issues/2316#issuecomment-867621727)
        * [#2496](https://github.com/xournalpp/xournalpp/issues/2496)

* If you are using an input device that is not pressure sensitive, the **Enable
  Pressure Inference** option can be used to guess pressure levels based on how
  quickly a stroke is drawn.

### Input Stabilization

The Input Stabilization feature can be enabled to draw smoother strokes.
This involves two parts: the _averaging method_ and the _preprocessor_.
Both are optional, but at least one should be enabled for smoothing to work.

If you do not want to spend too much time tweaking the settings, a good starting
point is to use `Velocity based Gaussian weights` averaging method and no
preprocessor.
You may want to enable a preprocessor if you are prone to jerking or jittering
your input device.

The averaging method is used to determine _how_ to smooth out the strokes.

* **Velocity based Gaussian weights** saves a running history of the input
  locations and directions, which then adjusts the final position of the next
  point to add to the stroke.
* **Arithmetic mean** smooths the strokes by saving the history of the last few
  input locations (determined by the `Buffersize` parameter) and adding the
  arithmetic mean of those points to the stroke.
  This averaging method draws nice, smooth strokes, but this means that the last
  few points cannot be added to the stroke until the stroke is finalized,
  causing a noticable sluggishness when drawing.

The preprocessor helps reduce the amount of jaggedness/jerkiness in a stroke:

* **Inertia** will reduce the amount of position change based on the speed at
  which the stroke is drawn (similar to how a spring works).
  This smooths strokes by reducing the effect of sudden jerking movements with
  the input device.
  The effect of the inertia preprocessor is determined by the parameters
  `Mass` (a constant amount of reduction) and `Drag` (reduction based on speed).
* **Deadzone** prevents small position changes from being added to the stroke,
  such as if the pen is jittered in the same location.
  The size of these "small" position changes is determined by the `Radius`
  parameter.

For technical details about how the input stabilization works, see [this comment
on
GitHub](https://github.com/xournalpp/xournalpp/issues/2320#issuecomment-739959511).

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

See the [TeX tool page](../tools/latex.md) for more information.

TODO

## Language

TODO
