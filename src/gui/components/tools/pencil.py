from .base.tool import Tool
from ..canvas import Canvas

from lib.draw_pixel import paint
from lib.primitives.lines.bresenham import draw_line

class Pencil(Tool):
    def __init__(self, canvas:Canvas):
        super().__init__(canvas)
        self.last_x = None
        self.last_y = None

    def on_press(self, x:int,y:int):
        self.last_x = x
        self.last_y = y
        paint(self.canvas.backbuffer, x,y, self.color, self.size)

    def on_drag(self, x0:int,y0:int, x1:int, y1:int):
        if self.last_x is None or self.last_y is None:
            self.last_x = x0
            self.last_y = y0

        draw_line(self.canvas.backbuffer, self.last_x,self.last_y, x1,y1, self.color, self.size)

        self.last_x = x1
        self.last_y = y1