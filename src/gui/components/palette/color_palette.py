from OpenGL.GL import *

from core.back_buffer import BackBuffer
from core.front_buffer import FrontBuffer

from .color_square import ColorSquare

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
        y = self.h - 145
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

    def render(self):
        glWindowPos2i(self.my_x_offset, 0)
        glDrawPixels(
            self.w,
            self.h,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            bytes(self.frontbuffer.pixels)
        )