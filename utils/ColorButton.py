from button import *


class ColorButton(Button):
    def __init__(self, x, y, width, height, color, text=None,
                 text_color=BLACK):
        Button.__init__(self, x, y, width, height, color, text,
                        text_color)
