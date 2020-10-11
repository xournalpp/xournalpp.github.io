# Tools & Editing

## Pen and Highlighter tools

The pen and highlighter tools allow you to **write**, **annotate** the document and **create various shapes** using a mouse or a pressure-sensitive stylus. Both pen and highlighter can be used with various colors and thicknesses. In fill mode the enclosed area will automatically be filled. The pen and highlighter tool can also draw various shapes (squares and rectangles, ellipses and circles, arrows, line segments, coordinate systems and splines) instead of strokes. Some of these shapes (line segments, rectangles and circles) can also be automatically recognized using the stroke recognizer.

- To change the **color** of any selected stroke or any future strokes you draw, click on one of the color buttons. Besides the preset color buttons, you can also set a custom color by clicking on the Select color button.
- The **fill mode** can be toggled by selecting the paint bucket icon (in the default layout, it is to the left of the color buttons).
- To change the **thickness**, press one of the thickness buttons (in the default layout, they are to the left of the fill bucket button).
- In order to draw **shapes** instead of strokes or to turn on the stroke recognizer use the shapes toggle menu, which you find to the right of the LaTeX tool (Math TEX button) in the default layout. The shapes toggle menu will have a dropdown arrow on its right.

The shape modes can be used as follows:

### Shapes defined by two points

- In order to draw a **line segment** or an **arrow** click at the location of the first point (tail) and drag the cursor to the location of the second end point (head).
- **Ellipses/circles** and **rectangles/squares** can be drawn in similar fashion. These shapes will be symmetrical with respect to the horizontal and vertical axis.
  The first point can be either the center of the shape or one of the corners (of the surrounding rectangle/square in case of an ellipsis/circle). The second point will always be one of the corners.
  Pressing the control key will make this shape been **drawn from the center**, pressing the shift key will make it a **perfect circle/square**. If you do not want to use the keyboard for these modifiers, you can activate the **drawing direction** modifiers in the preferences (drawing area panel). Draw UP from the start point if you want the start point to be the center of the shape. Draw LEFT from the start point if you want the shape to be a circle/square.
- The **coordinate system** is a simple L-shape. Modifiers can be applied like for ellipses/circles and rectangles/squares.

### Splines

The **Spline** shape is only available in version **1.1.0+dev**. With this shape you can draw polygon courses and smooth curves. Technically these curves are splines consisting of Bezier curve segments of degree at most 3.

In order to draw a **polygon course** you simply click (and immediately release) on the locations where you want the vertices of your polygon course. For drawing a **smooth curve** you should always drag the mouse/stylus a little after clicking on the locations through which the curve shall pass. The curve will be tangent to the direction you drag out at the chosen points though which the curve passes. You can also combine linear spline segments with curved segments.
The points where you click are called **anchor points** (or knots). They will be displayed with little red circles while editing the spline. The directions you drag out will be displayed as **tangents** in green color. Technically the two ends of the tangent are control points of the spline.

You have several ways of correcting the last anchor point and the last tangent.

- Press the **ARROW** keys to move the last anchor point around.
- Use the keys **r** (respecitvely **Shift + r**) to rotate the tangent (counter) clockwise.
- Use the keys **s** (respectively **Shift + s**) to scale the last tangent up or down.
- You can also completely remove the last anchor point (and the corresponding tangent) via the **BACKSPACE** key.

Drawing a spline is finished by either connecting the curve up to the first vertex/anchor point (yielding a closed spline), by double clicking or using the **ESCAPE** key.

### Stroke recognizer

If the **stroke recognizer** is turned on, it will attempt to convert every stroke upon completion into either

- a line segment,
- a circle or
- a (possibly rotated) rectangle/square.

It will leave the stroke as-is if it cannot match the stroke to one of these shapes.

## Eraser tool

The Eraser tool can remove strokes or parts of strokes. It has three modes:

- **Standard**: remove parts of strokes that the cursor moves over.
- **Whiteout**: paint a white stroke.
- **Delete Stroke**: remove the entirety of any stroke that the cursor touches.

## LaTeX Tool

Using the LaTeX tool you can insert LaTeX formulas into a Xournal++ document. In order to use this tool you must have LaTeX installed on your system.
The feature needs to be able to call pdflatex. In addition, the LaTeX `standalone` package needs to be installed, which typically requires installation of `texlive-latex-extra` or `texlive-standalone`. On Ubuntu or similar Linux systems this means

`sudo apt-get install texlive-latex-extra`

For other operating systems you will need to consult your LaTeX installation manual on how to add the standalone LaTeX package.

### Basic LaTeX formulas

Clicking on the LaTeX button in the toolbar will bring up a dialog which will allow you to type in a formula. A preview will be displayed in the center of the dialog, which will keep updating as you type and indicate whether your formula is valid. Once you are done, you can click the OK button to insert the LaTeX into the document; the rendered formula will appear at the center of the current page. The formula can be selected, moved scaled and edited as desired.

Note that the LaTeX formula will always be set in *inline math mode*. If you want to exit math mode, you should write a $-sign to leave math mode and add another $-sign at the end to reenter math-mode. For instance the LaTeX formula

```tex
$\huge$ x^2
```

will use the command `\huge` to increase the font size, which cannot be done in math mode.

### Enhanced LaTeX tool in Xournal++ 1.1.0+dev

The LaTeX tool has recently been extended making it much more configurable. Most importantly a customizable template has been implemented, where you can load packages and define macros. Moreover a LaTeX settings panel has been added, where you choose the template, specify the LaTeX generation command and test your LaTeX configuration. The extension is only available in version 1.1.0+dev.

#### Customization of the template

A default LaTeX template is provided under the name `default_template.tex`. By default it is pre-selected in the LaTeX settings panel. Clicking on it, you will find its location in your file system. On Linux systems it will typically be stored in
`/usr/share/xournalpp/resources`.

To generate a custom LaTeX template, make a copy of the default template, save it under a different name and start customizing it by adding packages and macros. Some suggestions are listed here:

- Include the [**graphicx** package](https://ctan.org/pkg/graphicx) by adding `\usepackage{graphicx}` to your template file. As an example this will give you the possibility to add rotated text via a LaTeX formula like

```tex
\text{\rotatebox[origin=c]{90}{My Rotated Text}}
```

- Include the [**TikZ** package](https://www.ctan.org/pkg/pgf) via `\usepackage{tikz}` for creating drawings with the powerful TikZ tool. A simple example would be to draw a table (or grid) with n rows and m columns via `\tikz{\draw (0,0) grid(m,n)}`. See [this issue](https://github.com/xournalpp/xournalpp/issues/2179) for more information.

- Include the [**PGFPlots** package](https://www.ctan.org/pkg/pgfplots) via `\usepackage{pgfplots}` for plotting function graphs. Using a macro you will be able to plot function graphs nicely and very quickly. For example, add the following lines to your template:

```teX
%for defining commands
\usepackage{xargs}

% for drawing and plotting
\usepackage{pgfplots}
\pgfplotsset{compat=newest} % Allows to place the legend below plot
\newcommandx{\graph}[3][1=,2=]{
    \begin{tikzpicture}
    \begin{axis}[xlabel=$x$,ylabel=$y$, axis lines=center,samples=100, #2]
    \addplot[#1]{#3};
    \end{axis}
    \end{tikzpicture}
}
```

Then a LaTeX-formula like `\graph{x^2}` will plot the normal parabola and `\graph[domain=-2:2, blue][x=1cm,y=1cm]{x^2}` will further restrict the domain, set the color and define units.

- Include the [**Listings** package](https://www.ctan.org/pkg/listings) via `\usepackage{listings}` for proper alignment and syntax coloring of code snippets. You need to define the style with `lstset` as in the following example, which you can add to your template:

```tex
\usepackage{listings}
\lstset{language=C++,
                basicstyle=\ttfamily,
                keywordstyle=\color{blue}\ttfamily,
                stringstyle=\color{red}\ttfamily,
                commentstyle=\color{green}\ttfamily,
                morecomment=[l][\color{magenta}]{\#}
}
```

In the LaTeX formula you can then use the `lstlistings` enivronment as in the following example

```tex
\begin{lstlisting}
#include<stdio.h>
#include<iostream>
// A comment
int main(void)
{
    printf("Hello World\n");
    return 0;
}
\end{lstlisting}
```
