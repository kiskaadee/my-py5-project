import math

# pyright: reportUndefinedVariable=false
# Para Lu ✨


def setup():
    size(400, 400)
    background(255, 200, 200)  # Soft pink background

    # Move the drawing origin to the center of the screen
    # Otherwise, the heart will be cut off at the top-left (0,0)
    translate(width / 2, height / 2)

    no_stroke()
    fill(220, 20, 60)  # Crimson Red

    # We use begin_shape() to create a custom polygon from our points
    begin_shape()

    # t goes from 0 to 2*PI (a full circle of points)
    # We use a small step (0.1) for a smooth curve
    t = 0
    while t < math.tau:  # tau is 2 * PI
        # The Parametric Equations:
        # Scale factor (10) makes the heart visible (otherwise it's only 16 pixels wide!)
        x = 16 * math.sin(t) ** 3
        y = -(
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        # Plot the vertex
        vertex(x * 10, y * 10)

        t += 0.05

    end_shape(CLOSE)
