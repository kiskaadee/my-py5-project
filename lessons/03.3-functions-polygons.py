# Shapes and Vertex: Custom Geometry & Polygons
# pyright: reportUndefinedVariable=false
import random


def setup():
    size(980, 980)
    background(16, 124, 16)  # Xbox Green

    # MENTAL MODEL: Static Placement
    # These are called once. Their 'random' or 'frame_count' values
    # are locked in the moment setup() finishes.
    no_stroke()
    draw_xbox_star(width / 2, height / 2, 300, 100)

    stroke(0)
    # Tony's Star: Demonstrates angular iteration
    draw_star_tony(800, 800, outer_radius=150, inner_radius=40, num_points=8)

    # Abstract Poly: Demonstrates vertex displacement (noise/randomness)
    draw_abstract_poly(200, 200, radius=150, num_vertices=6)


def draw_abstract_poly(center_x, center_y, radius, num_vertices):
    """
    Mental Model: Vertex Displacement.
    We calculate a perfect circle but 'nudge' each point randomly
    before committing it to the shape.
    """
    stroke(0)
    stroke_weight(2)
    fill(100, 140, 255, 150)  # Blue with Alpha transparency

    begin_shape()  # Start the path 'recording'
    for i in range(num_vertices):
        angle = (TAU / num_vertices) * i
        # Adding 'jitter' to the radius creates the abstract look
        offset = random.uniform(-20, 20)

        vx = center_x + cos(angle) * (radius + offset)
        vy = center_y + sin(angle) * (radius + offset)
        vertex(vx, vy)
    end_shape(CLOSE)  # Connect the last dot to the first


def draw_star_tony(cx, cy, outer_radius, inner_radius, num_points, start_angle=0):
    """
    Mental Model: Alternating Radii.
    A star is just a polygon that alternates between a 'far' distance
    and a 'near' distance from the center.
    """
    angle_step = TWO_PI / num_points
    begin_shape()
    for i in range(num_points):
        # Current 'tip' angle
        # Note: frame_count here is captured once if called in setup()
        current_angle = start_angle + angle_step * i + frame_count / 50.0

        # 1. Outer Point (The Tip)
        ax = cx + cos(current_angle) * outer_radius
        ay = cy + sin(current_angle) * outer_radius
        vertex(ax, ay)

        # 2. Inner Point (The Valley)
        # We offset the angle by half a step to put the valley between tips
        bx = cx + cos(current_angle + angle_step / 2.0) * inner_radius
        by = cy + sin(current_angle + angle_step / 2.0) * inner_radius
        vertex(bx, by)
    end_shape(CLOSE)


def draw_xbox_star(center_x, center_y, size_a, size_b):
    """
    Mental Model: Manual Coordinate Mapping.
    Instead of math, we define a list of relative 'offsets'
    and apply them to a center point.
    """
    # Hardcoded relative coordinates
    points_list: list[tuple] = [
        (-size_a, -size_a),
        (0, -size_b),
        (size_a, -size_a),
        (size_b, 0),
        (size_a, size_a),
        (0, size_b),
        (-size_a, size_a),
        (-size_b, 0),
    ]

    begin_shape()
    for rel_x, rel_y in points_list:
        # Transforming relative coordinates to screen coordinates
        vertex(center_x + rel_x, center_y + rel_y)
    end_shape(CLOSE)


# --- TUTORIAL REVIEW ---
# 1. Path State: begin_shape() opens a buffer. vertex() fills it.
#    end_shape() flushes that buffer to the GPU to be drawn.
# 2. Geometry via Math: cos() and sin() are the engines of circular geometry.
#    x = center + cos(a) * r | y = center + sin(a) * r
# 3. The 'CLOSE' argument: Without it, the shape is a 'line string'.
#    With it, it becomes a 'closed polygon' that can be filled.
