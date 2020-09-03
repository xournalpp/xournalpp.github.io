# Tools & Editing

TODO

## Constructing Tables
I wasn't aware of the ability to add tables in xournalpp until I was shown the power of the built in latex editor. You can add to the latex preamble (edit the default_template.tex in the settings) to contain `\usepackage{tikz}` so that we have access to the powerful `tikz` package. Now we can create n by m sized tables, for example we can insert this code to obtain a 7 by 4 table: `\tikz{\draw (0,0) grid(7,4)}`. For more information read the original issue: https://github.com/xournalpp/xournalpp/issues/2179
