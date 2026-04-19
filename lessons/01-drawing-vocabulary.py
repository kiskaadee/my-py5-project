# Initial py5 drawing vocabulary
# pyright: reportUndefinedVariable=false


def setup():
    size(500, 500)  # here we define the size of our window
    background(
        200, 0, 200
    )  # this defines background properties. In this case, the three rgb components of background color
    # rect_mode(CENTER)
    # all properties
    fill(0, 200, 0)  # declares the color of the next shape
    # no_stroke()  # removes the default border
    stroke(255, 0, 0)  # turns the border to red
    stroke_weight(5)  # apply modifier for border weight
    rect(width / 2, height / 2, 200, 50)

    ## rectangle has been plotted.
    # new properties will now apply to the next element to render in the loop
    no_stroke()
    fill(255, 255, 0)
    ellipse(200, 100, 300, 50)
