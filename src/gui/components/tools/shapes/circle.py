from ..base.tool import Tool
from ...canvas import Canvas

from lib.others.shapes.circle.from_center import draw_circle
from lib.others.fill.uniform import flood_fill

class Circle(Tool):
    def __init__(self, canvas:Canvas):
        super().__init__(canvas)
        self.is_filled = False

        self.center_x = None
        self.center_y = None

    def on_press(self, x, y):
        self.center_x = x
        self.center_y = y

    def on_drag(self, x0:int,y0:int, x1:int,y1:int):
        self.canvas.current_edit_clear()
        draw_circle(self.canvas.backbuffer, x0,y0, x1,y1, self.color, self.size)

    def switch_is_filled(self):
        self.is_filled = not self.is_filled

    def on_release(self):
        if self.is_filled:
            flood_fill(self.canvas.backbuffer, self.center_x, self.center_y, self.color)
        self.canvas.upload_backbuffer()