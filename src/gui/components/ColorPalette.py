from OpenGL.GL import *

from core.BackBuffer import BackBuffer
from core.FrontBuffer import FrontBuffer

class ColorSquare:
    def __init__(self, x:int,y:int, side:int, color:tuple[int,int,int,int]):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def is_inside(self, px, py):
        return (self.x <= px < self.x + self.side) and (self.y <= py < self.y + self.side)

    def draw(self, buffer):
        for y in range(self.y, self.y + self.side):
            for x in range(self.x, self.x + self.side):
                buffer.put_pixel(x, y, self.color)

class ColorPalette:
    def __init__(self, width:int,height:int, square_side:int, my_x_offset): 
        self.w = width
        self.h = height
        self.square_side = square_side

        self.my_x_offset = my_x_offset

        self.frontbuffer = FrontBuffer(self.w,self.h, (62,62,62,255))
        self.backbuffer = BackBuffer(self.frontbuffer)

        self.squares: ColorSquare = []

        self.colors = [
            (0,0,0,255),
            (255,0,0,255),
            (0,255,0,255),
            (0,0,255,255),
            (255,255,0,255),
            (0,255,255,255),
            (255,0,255,255),
            (124,124,124,255)
        ]
        self.create_squares()

    def create_squares(self):
        y = self.h - 80
        x = (self.w - self.square_side) // 2

        for color in self.colors:
            square = ColorSquare(x,y, self.square_side, color)
            self.squares.append(square)
            square.draw(self.backbuffer
                        )
            y -= self.square_side + 10
        self.backbuffer.commit()

    def get_color(self, x, y):
        x -= self.my_x_offset
        for square in self.squares:
            if square.is_inside(x, y):
                return square.color
        return None


    def render(self, window_total_h:int):
        y_offset = window_total_h - self.h

        glWindowPos2i(self.my_x_offset, y_offset)
        glDrawPixels(
            self.w,
            self.h,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            bytes(self.frontbuffer.pixels)
        )