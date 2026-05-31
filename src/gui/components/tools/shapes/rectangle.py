from ..base.tool import Tool
from ...canvas import Canvas

from lib.others.shapes.rectangle.bresenham import draw_rectangle
from lib.others.fill.uniform import flood_fill


class Rectangle(Tool):
    def __init__(self, canvas:Canvas):
        super().__init__(canvas)
        self.is_filled = False

        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

    def on_press(self, x, y):
        self.start_x = x
        self.start_y = y

    def on_drag(self, x0:int,y0:int, x1:int,y1:int):
        self.canvas.current_edit_clear()
        draw_rectangle(self.canvas.backbuffer, x0,y0, x1,y1, self.color, self.size)
        self.end_x = x1
        self.end_y = y1

    def switch_is_filled(self):
        self.is_filled = not self.is_filled

    def on_release(self):
        if self.is_filled:
            mid_x = (self.start_x + self.end_x) // 2
            mid_y = (self.start_y + self.end_y) // 2

            flood_fill(self.canvas.backbuffer, mid_x, mid_y, self.color)
        self.canvas.upload_backbuffer()
