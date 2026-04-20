# Initial py5 drawing vocabulary
# pyright: reportUndefinedVariable=false


def setup():
    # 1. Coordinate System & Canvas
    # size() defines the width and height of the window in pixels.
    # This also initializes the system variables 'width' and 'height'.
    size(500, 500)

    # 2. The Background
    # background() fills the entire canvas. Calling it once in setup()
    # means we are painting the "paper" before we start drawing shapes.
    background(200, 0, 200)  # RGB: A deep purple/magenta

    # 3. Setting the "State" for the first shape
    # Think of these as picking up a specific brush and paint color.
    fill(0, 200, 0)  # Set the interior 'paint' color to Green
    stroke(255, 0, 0)  # Set the 'pen' color for the outline to Red
    stroke_weight(5)  # Set the thickness of the 'pen' line

    # 4. Drawing the Shape
    # rect(x, y, w, h)
    # MENTAL MODEL: The "Anchor Point".
    # By default, py5 uses 'rect_mode(CORNER)', meaning the (x, y)
    # you provide is the top-left corner.
    # width/2 and height/2 use the system variables to find the canvas center.
    rect(width / 2, height / 2, 200, 50)
    # 5. Updating the "State" (The "State Machine" Logic)
    # We must explicitly change the settings, or the next shape will
    # still be Green with a Red 5px border.
    no_stroke()  # Disables the outline entirely for subsequent shapes
    fill(255, 255, 0)  # Switches the 'paint' color to Yellow

    # 6. Drawing the next shape
    # MENTAL MODEL: Ellipses default to 'ellipse_mode(CENTER)'.
    # Unlike the rectangle above, this (x, y) is the middle of the shape.
    ellipse(200, 100, 300, 50)


# TUTORIAL SUMMARY:
# - States: fill(), stroke(), and stroke_weight() are 'sticky'. They stay
#   active until you overwrite them.
# - Defaults: Rectangles draw from CORNER; Ellipses draw from CENTER.
# - Math: You can perform operations inside arguments (like width / 2).
