from gui.components.Canvas import Canvas

from lib.primitives.lines.bresenham import draw_line
from lib.draw_pixel import draw_pixel

class Tool:
    def on_press(self, canvas:Canvas, x:int,y:int, color:tuple):
        pass
    def on_drag(self, canvas:Canvas, x0:int,y0:int, x1:int,y1:int, color:tuple):
        pass
    def on_release(self, canvas:Canvas):
        canvas.upload_backbuffer()


class Pencil(Tool):
    def __init__(self, size:int):
        self.last_x = None
        self.last_y = None
        self.size = size

    def on_press(self, canvas, x:int,y:int, color):
        self.last_x = x
        self.last_y = y
        draw_pixel(canvas.backbuffer, x,y, color, self.size)
    
    def on_drag(self, canvas, x0:int,y0:int, x1:int, y1:int, color):
        draw_line(canvas.backbuffer, self.last_x, self.last_y, x1,y1, color, self.size)

        self.last_x = x1
        self.last_y = y1

class Line(Tool):
    def __init__(self, size:int):
        self.size = size

    def on_drag(self, canvas:Canvas, x0:int,y0:int, x1:int,y1:int, color:tuple):
        canvas.current_edit_clear()
        draw_line(canvas.backbuffer, x0,y0, x1,y1, color, self.size)