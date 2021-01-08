
# Pen and Highlighter tools

The pen and highlighter tools allow you to **write**, **annotate** the document and **create various shapes** using a mouse or a pressure-sensitive stylus. Both pen and highlighter can be used with various colors and thicknesses. In fill mode the enclosed area will automatically be filled. The pen and highlighter tool can also draw various shapes (squares and rectangles, ellipses and circles, arrows, line segments, coordinate systems and splines) instead of strokes. Some of these shapes (line segments, rectangles and circles) can also be automatically recognized using the stroke recognizer.

- To change the **color** of any selected stroke or any future strokes you draw, click on one of the color buttons. Besides the preset color buttons, you can also set a custom color by clicking on the Select color button.
- The **fill mode** can be toggled by selecting the paint bucket icon (in the default layout, it is to the left of the color buttons).
- To change the **thickness**, press one of the thickness buttons (in the default layout, they are to the left of the fill bucket button).
- In order to draw **shapes** instead of strokes or to turn on the stroke recognizer use the shapes toggle menu, which you find to the right of the LaTeX tool (Math TEX button) in the default layout. The shapes toggle menu will have a dropdown arrow on its right.

The shape modes can be used as follows:

## Shapes defined by two points

- In order to draw a **line segment** or an **arrow** click at the location of the first point (tail) and drag the cursor to the location of the second end point (head).
- **Ellipses/circles** and **rectangles/squares** can be drawn in similar fashion. These shapes will be symmetrical with respect to the horizontal and vertical axis.
  The first point can be either the center of the shape or one of the corners (of the surrounding rectangle/square in case of an ellipsis/circle). The second point will always be one of the corners.
  Pressing the control key will make this shape been **drawn from the center**, pressing the shift key will make it a **perfect circle/square**. If you do not want to use the keyboard for these modifiers, you can activate the **drawing direction** modifiers in the preferences (drawing area panel). Draw UP from the start point if you want the start point to be the center of the shape. Draw LEFT from the start point if you want the shape to be a circle/square.
- The **coordinate system** is a simple L-shape. Modifiers can be applied like for ellipses/circles and rectangles/squares.

## Splines

The **Spline** shape is only available in version **1.1.0+dev**. With this shape you can draw polygon courses and smooth curves. Technically these curves are splines consisting of Bezier curve segments of degree at most 3.

In order to draw a **polygon course** you simply click (and immediately release) on the locations where you want the vertices of your polygon course. For drawing a **smooth curve** you should always drag the mouse/stylus a little after clicking on the locations through which the curve shall pass. The curve will be tangent to the direction you drag out at the chosen points though which the curve passes. You can also combine linear spline segments with curved segments.
The points where you click are called **anchor points** (or knots). They will be displayed with little red circles while editing the spline. The directions you drag out will be displayed as **tangents** in green color. Technically the two ends of the tangent are control points of the spline.

You have several ways of correcting the last anchor point and the last tangent.

- Press the **ARROW** keys to move the last anchor point around.
- Use the keys **r** (respecitvely **Shift + r**) to rotate the tangent (counter) clockwise.
- Use the keys **s** (respectively **Shift + s**) to scale the last tangent up or down.
- You can also completely remove the last anchor point (and the corresponding tangent) via the **BACKSPACE** key.

Drawing a spline is finished by either connecting the curve up to the first vertex/anchor point (yielding a closed spline), by double clicking or using the **ESCAPE** key.

## Stroke recognizer

If the **stroke recognizer** is turned on, it will attempt to convert every stroke upon completion into either

- a line segment,
- a circle or
- a (possibly rotated) rectangle/square.

It will leave the stroke as-is if it cannot match the stroke to one of these shapes.
