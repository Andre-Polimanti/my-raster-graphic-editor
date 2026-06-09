from ..tools.base.tool import Tool
from ..canvas import Canvas

from lib.primitives.lines.bresenham import draw_line

class Line(Tool):
    def __init__(self, canvas:Canvas):
        super().__init__(canvas)

    def on_drag(self, x0:int,y0:int, x1:int,y1:int):
        
        self.canvas.current_edit_clear()
        draw_line(self.canvas.backbuffer, x0,y0, x1,y1, self.color, self.size)