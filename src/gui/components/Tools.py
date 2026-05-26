from gui.components.Canvas import Canvas

from lib.primitives.lines.bresenham import draw_line
from lib.draw_pixel import draw_pixel

class Tool:
    def __init__(self, canvas:Canvas):
        self.canvas = canvas
        self.color = (0,0,0,255)
        self.size = 0
        pass

    def on_press(self, x:int,y:int): pass
    def on_drag(self, x0:int,y0:int, x1:int,y1:int): pass    

    def set_size(self, new_size:int):
        self.size = new_size
    def set_color(self, selected_color:tuple):
        self.color = selected_color

    def on_release(self):
        self.canvas.upload_backbuffer()

class Pencil(Tool):
    def __init__(self, canvas:Canvas):
        super().__init__(canvas)
        self.last_x = None
        self.last_y = None

    def on_press(self, x:int,y:int):
        self.last_x = x
        self.last_y = y
        draw_pixel(self.canvas.backbuffer, x,y, self.color, self.size)

    def on_drag(self, x0:int,y0:int, x1:int, y1:int):
        if self.last_x is None or self.last_y is None:
            self.last_x = x0
            self.last_y = y0

        draw_line(self.canvas.backbuffer, self.last_x,self.last_y, x1,y1, self.color, self.size)

        self.last_x = x1
        self.last_y = y1

class Eraser(Pencil):
    def __init__(self,canvas:Canvas):
        super().__init__(canvas)
        self.color = (self.canvas.frontbuffer.bg_color)

class Line(Tool):
    def __init__(self, canvas:Canvas):
        super().__init__(canvas)

    def on_drag(self, x0:int,y0:int, x1:int,y1:int):
        self.canvas.current_edit_clear()
        draw_line(self.canvas.backbuffer, x0,y0, x1,y1, self.color, self.size)
