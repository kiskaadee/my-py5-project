# Python loops, lines and patterns
# pyright: reportUndefinedVariable=false

# We calculate these once outside of setup/draw for efficiency
N: int = 50
primes: list[int] = [
    x for x in range(2, N) if all(x % d != 0 for d in range(2, int(x**0.5) + 1))
]


def setup():
    size(980, 980)
    background(255, 200, 100)  # Warm orange/yellow background

    # 1. Prime-based Distribution
    # The 'n' acts as the X-coordinate for the start of the line.
    stroke(0, 50)  # Black with low opacity (Alpha) to see overlapping lines
    for n in primes:
        # Drawing a line from top (y=0) to bottom (y=height)
        # Using n**2 to create a non-linear "fanning" effect
        line(n * 10, 0, n**2, height)

    # 2. Linear Progression (The "Fan" effect)
    stroke(255, 0, 0)  # Red lines
    stroke_weight(1)
    for n in range(10, 70, 2):
        # n*10 moves the top point linearly
        # n*5 moves the bottom point at a different speed, creating the tilt
        line(n * 10, 100, n * 5, 490)

    # 3. Margin & Offset Loop
    # This is the standard way to create a series of parallel or related lines
    margin = 50
    stroke(0, 0, 255)  # Blue lines
    for i in range(20):
        # x1 increases by 8 pixels each loop
        # x2 increases by 16 pixels each loop (stretching out)
        line(margin + i * 8, 600, margin + i * 16, 900)

    # 4. A Color Gradient Loop
    # Position is only one of the parameters that can be modified through iterations
    # Using a loop to change the 'State' (color) as we draw
    for i in range(0, width, 20):
        stroke(i / 2, 100, 150)  # Stroke color changes based on the X position
        stroke_weight(2)
        line(i, 0, i, 50)  # A small "comb" pattern at the top
