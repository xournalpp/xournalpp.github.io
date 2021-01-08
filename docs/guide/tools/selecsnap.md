# Selection & Snapping tools

## Selection tools

With the selection tools you can either select a single object or multiple objects of the page in order to interact with them. Specifically the following interactions and objects are supported:

- **Strokes**: can be copied, cut, erased, moved, resized, and rotated.
- **Images, LaTeX and text**: can be copied, cut, deleted, moved and resized.
- **Pdf**: currently not compatible with any selection tool.

Object selection can be done with one of the following tools:

- **Select Rectangle**: creates a rectangular region from a corner while dragging and selecting all objects strictly within it.

- **Select region**: works like a pen, where your stroke creates a shadow around the region you enclose. Again, all objects must be completely covered with this shadow to be included in the selection.

- **Select object**: select only one object at a time. You just need to touch the object to select.

When an object is clicked with the **Select Region** or **Select Rectangle** tool, the touched object is selected; that is, they work like the object selection tool.
You can simplify the selection of single objects by enabling `Tap action` in the preferences (drawing area panel) and the "Try to select object first" checkbox. If activated you can select single objects simply by tapping (short clicking) on them regardless of the tool that is currently in use.

## Snapping tools

The Snapping tools correct and adjust the displacement, size and rotation angle of selected objects. Drawing of shapes and (optionally) recognized shapes are also affected.

### Grid Snapping

Grid Snapping makes the displacements of objects and lines made with the tools mentioned above fit with the grid of the page. This grid matches **by default** the _Graph_ background grid, but it continues to exist internally even with other backgrounds.
When you resize with Grid Snap enabled, the resize will attempt to match the grid line, no matter which side of the object. Similarly if you displace a selection by dragging it, it will attempt to match a grid point. Hold the selection near the corner that needs to be matched. Technically Xournal++ computes a minimal rectangle that contains all the objects of the selection. This rectangle is a bit smaller than the one you get display for manipulating the selection. The corner of this smaller rectangle which is closest to the cursor position will get matched.


### Rotation Snapping

Rotation Snapping allows rotations of selected objects and strokes made with the tools mentioned above to be snapped to predetermined angles. These default angles correspond to multiples of 15 degrees. This allows you e.g. to easily rotate some strokes or shapes around 45 degrees, 60 degrees or 90 degrees.

### Configuration

Both tools have a tolerance that can be configured in the preferences (Drawing Area panel, section Snapping). Higher values correspond to greater intensity in the effect. On the extrema, tolerance 1.0 means that all objects will get snapped; tolerance 0.0 means that no objects will get snapped. 

The Snapping effect is disabled by default for shape recognition, but it can be activated in the same section.

Note that in the Grid Snapping description it is mentioned that the grid matches **by default** the grid of the _Graph_ background. This grid consists of squares with side length 0.5 cm. By means of the **Grid size** parameter it is possible to change the side length of the grid squares as a multiple of the original length.

In this way, for example, by setting 0.5 in the parameter, the internal grid becomes squares half the size of the Graph paper grid background, so the objects will try to fit not only the lines of the squares, but also with its halves.
