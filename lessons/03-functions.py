# Modular Drawing with Functions
# pyright: reportUndefinedVariable=false


def setup():
    # Setting up a large canvas for our repeated patterns
    size(980, 980)
    background(40, 30, 40)  # Dark charcoal background

    # Using a loop to call our custom function multiple times
    # This demonstrates the power of modularity:
    # Change the function code once, and every eye on the screen updates.
    for y in range(150, 900, 150):
        # We pass arguments to the parameters (x, y, w)
        eye(width / 2, y, 200)

        # We can even call it with different sizes or offsets in the same loop
        eye(width / 4, y, 100)
        eye(3 * width / 4, y, 100)


def eye(x: float, y: float, w: float):
    """
    Draws a stylized eye centered at (x, y) with a total width of (w).

    The 'Mental Model' for creating custom drawing functions:
        1. Local Scope: x,y, and w only exists within this function's scope
        2. Proportional Drawing: Every part of the eye is calculated relative to 'w' so it scales perfectly
    """

    # --- Layer 1: The Sclera ---
    no_stroke()
    fill(255)  # white
    # ellipse(
    #     a: float,  # x-coordinate of the ellipse
    #     b: float,  # y-coordinate of the ellipse
    #     c: float,  # width of the ellipse by default
    #     d: float,  # height of the ellipse by default
    #     /,
    # ) -> None
    # Our height is 1/3 of the width to create an almond shape
    ellipse(x, y, w, w / 3)

    # --- Layer 2: The Iris ---
    fill(128, 64, 0)  # brown
    # the iris is a circle with diameter equal to the sclera's height
    ellipse(x, y, w / 3, w / 3)

    # --- Layer 3: The Pupil ---
    fill(0)  # black
    # smallest detal, 10% of the total width
    ellipse(x, y, w / 10, w / 10)


# TUTORIAL REVIEW:
# 1. Abstraction: The setup() doesn't need to know how to draw an eye;
#    it just needs to know where to put it.
# 2. Parameters: 'x', 'y', and 'w' act as placeholders. When we call
#    eye(500, 200, 150), 500 is assigned to x, 200 to y, and 150 to w.
# 3. DRY Principle: "Don't Repeat Yourself." If you want to change
#    the iris color to blue, you only change one line inside eye().
