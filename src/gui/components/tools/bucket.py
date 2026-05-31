from ..tools.base.tool import Tool
from ..canvas import Canvas

from lib.others.fill.uniform import flood_fill

class Bucket(Tool):
    def __init__(self, canvas:Canvas):
        super().__init__(canvas)

    def on_press(self, x, y):
        flood_fill(self.canvas.frontbuffer, x,y, self.color)

    def on_release(self):
        pass
