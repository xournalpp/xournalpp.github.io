# LaTeX tool

Using the LaTeX tool you can insert LaTeX formulas into a Xournal++ document. In order to use this tool you must have LaTeX installed on your system.
The feature needs to be able to call pdflatex. In addition, the LaTeX `standalone` package needs to be installed, which typically requires installation of `texlive-latex-extra` or `texlive-standalone`. On Ubuntu or similar Linux systems this means

`sudo apt-get install texlive-latex-extra`

For other operating systems you will need to consult your LaTeX installation manual on how to add the standalone LaTeX package.

## Basic LaTeX formulas

Clicking on the LaTeX button in the toolbar will bring up a dialog which will allow you to type in a formula. A preview will be displayed in the center of the dialog, which will keep updating as you type and indicate whether your formula is valid. Once you are done, you can click the OK button to insert the LaTeX into the document; the rendered formula will appear at the center of the current page. The formula can be selected, moved scaled and edited as desired.

Note that the LaTeX formula will always be set in *inline math mode*. If you want to exit math mode, you should write a $-sign to leave math mode and add another $-sign at the end to reenter math-mode. For instance the LaTeX formula

```tex
$\huge$ x^2
```

will use the command `\huge` to increase the font size, which cannot be done in math mode.

## Enhanced LaTeX tool in Xournal++ 1.1.0+dev

The LaTeX tool has recently been extended making it much more configurable. Most importantly a customizable template has been implemented, where you can load packages and define macros. Moreover a LaTeX settings panel has been added, where you choose the template, specify the LaTeX generation command and test your LaTeX configuration. The extension is only available in version 1.1.0+dev.

## Customization of the template

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
    \addplot[#1]{ #3 };
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
$
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
$
```

Note that the starting and trailing $-signs are needed to exit and reenter math mode.
