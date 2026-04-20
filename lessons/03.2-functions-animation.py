# Animation and Interaction
# pyright: reportUndefinedVariable=false


def setup():
    size(980, 980)
    # Background in setup acts as the initial "primer"
    background(40, 30, 40)


def draw():
    # MENTAL MODEL: The "Clean Slate"
    # If you comment out the line below, the eyes will "smear"
    # across the screen because the old frames aren't being erased.
    background(40, 30, 40)

    # Interaction: System Variables
    # mouse_x and mouse_y are updated by py5 automatically.
    # By adding/subtracting from mouse_x, we create a fixed offset (the interpupillary distance).
    eye(mouse_x - 100, mouse_y, 150)
    eye(mouse_x + 100, mouse_y, 150)


def eye(x: float, y: float, w: float):
    """Draws a stylized eye centered at (x, y)"""
    no_stroke()
    fill(255)
    ellipse(x, y, w, w / 3)  # Sclera
    fill(128, 64, 0)
    ellipse(x, y, w / 3, w / 3)  # Iris
    fill(0)
    ellipse(x, y, w / 10, w / 10)  # Pupil


# --- 03.1 TUTORIAL NOTES ---
# 1. THE REFRESH RATE:
#    By default, draw() runs 60 times per second. This is your "Frame Rate."
#
# 2. SYSTEM VARIABLES:
#    Variables like 'mouse_x', 'mouse_y', and 'frame_count' are reserved by py5.
#    They provide a bridge between the physical world (your hand) and the digital canvas.
#
# 3. INTERACTIVE OFFSET:
#    Notice eye(mouse_x - 100, ...). By using math on a system variable,
#    you create "Parent-Child" relationships where the eyes follow the mouse
#    but maintain their own relative structure.
