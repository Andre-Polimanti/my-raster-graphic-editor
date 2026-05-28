from .Canvas import Canvas

from lib.primitives.lines.bresenham import draw_line
from lib.DrawPixel import draw_pixel

from lib.others.Circle import draw_circle
from lib.others.Rectangle import draw_rectangle

from lib.others.FloodFill import flood_fill



class Tool:
    def __init__(self, canvas:Canvas):
        self.canvas = canvas
        self.color = (0,0,0,255)
        self.size = 0

    def on_press(self, x:int,y:int): pass
    def on_drag(self, x0:int,y0:int, x1:int,y1:int): pass

    def set_size(self, new_size:int):
        self.size = new_size

    def set_color(self, selected_color:tuple):
        if selected_color:
            self.color = selected_color

    def on_release(self):
        self.canvas.upload_backbuffer()

    def switch_is_filled(self):
        pass

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
        
    def set_color(self, selected_color:tuple): pass
    
class Line(Tool):
    def __init__(self, canvas:Canvas):
        super().__init__(canvas)

    def on_drag(self, x0:int,y0:int, x1:int,y1:int):
        self.canvas.current_edit_clear()
        draw_line(self.canvas.backbuffer, x0,y0, x1,y1, self.color, self.size)

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

class Bucket(Tool):
    def __init__(self, canvas:Canvas):
        super().__init__(canvas)

    def on_press(self, x, y):
        flood_fill(self.canvas.frontbuffer, x,y, self.color)

    def on_release(self):
        pass
