from OpenGL.GL import *

from core.FrontBuffer import FrontBuffer
from core.BackBuffer import BackBuffer

from lib.others.Circle import draw_circle
from lib.others.Rectangle import draw_rectangle

from lib.primitives.lines.bresenham import draw_line

class Button:
    def __init__(self, x:int, y:int, side:int, func):
        self.x = x
        self.y = y

        self.side = side
        self.func = func

        self.mid_point = self.side//2

    def was_clicked(self, px:int,py:int):
        return (self.x - self.mid_point <= px <= self.x + self.mid_point) and (self.y - self.mid_point <= py <= self.y + self.mid_point)
    
    def draw(self, buffer):
        x0 = self.x - self.mid_point
        y0 = self.y + self.mid_point

        x1 = self.x + self.mid_point
        y1 = self.y - self.mid_point

        draw_rectangle(buffer, x0,y0, x1,y1, (0,0,0,255), 1)
        
        if(self.func == "Clear"):
            draw_x(buffer, x0,y0, x1,y1, (255,0,0,255), 1)

        elif(self.func == "Save"):
            r = self.mid_point
            pad = 5
            draw_circle(buffer, self.x, self.y, (self.x + r)-pad, self.y+pad, (0,255,0,255), 1)


class ButtonList:
    def __init__(self, width:int,height:int, my_x_offset:int):
        self. x0 = my_x_offset
        self.w = width
        self.h = height

        self.current_y = self.h - 60
        self.whole_window_width = self.w + self.x0

        self.frontbuffer = FrontBuffer(self.w,self.h, (62,62,62,255))
        self.backbuffer = BackBuffer(self.frontbuffer)

        self.buttons = self.create_buttons()

        for button in self.buttons:
            button.draw(self.backbuffer)
        
        self.backbuffer.commit()


    def create_buttons(self):
        side = self.w // 2
        center_x = self.w // 2
        
        clear_y = self.current_y
        save_y = self.current_y - side - 60

        clear_button = Button(center_x, clear_y, side, "Clear")
        save_button = Button(center_x, save_y, side, "Save")

        return [clear_button, save_button]

    def render(self):
        glWindowPos2i(self.x0,0)
        glDrawPixels(
            self.w,
            self.h,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            bytes(self.frontbuffer.pixels)
        )

def draw_x(buffer, x1:int,y1:int, x2:int,y2:int, color:tuple, size:int):
    pad = 10

    draw_line(buffer, x1 + pad, y1 - pad, x2 - pad, y2 + pad, color, size)
    draw_line(buffer, x1 + pad, y2 + pad, x2 - pad, y1 - pad, color, size)