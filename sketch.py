# confirming Py5 is installed and running
import py5

print("Hello from my-py5-project!")


def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.background(240)
    py5.fill(255, 0, 0)
    py5.rect(200, 200, 100, 100)


if __name__ == "__main__":
    py5.run_sketch()
