# pyright: reportUndefinedVariable=false


def settings():
    size(600, 600)


def setup():
    rect_mode(CENTER)
    # Essential for Arch/Wayland to prevent stuttering
    hint(DISABLE_TEXTURE_MIPMAPS)


def draw():
    background(30)
    fill(0, 255, 200)
    # The runner makes these live and global automatically
    square(mouse_x, mouse_y, 50)
