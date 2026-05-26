from OpenGL.GL import *

from core.BackBuffer import BackBuffer
from core.FrontBuffer import FrontBuffer

class ColorPalette:
    def __init__(self, width:int,height:int, color_square_d:int): 
        self.w = width
        self.h = height
        self.color_square_d = color_square_d

        self.frontbuffer = FrontBuffer(self.w,self.h, (62,62,62,255))
        self.backbuffer = BackBuffer(self.frontbuffer)
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

    def color_grid_coordenates(self):
        centers = []
        x_center = (self.w - 1) // 2
        y_start = self.h - 40
        spacing = 5

        for _ in self.colors:
            y = y_start - (self.color_square_d // 2)
            centers.append((x_center, y))
            y_start -= (self.color_square_d + spacing)

        return centers
    
    def create_squares(self):
        centers = self.color_grid_coordenates()
        half_d = self.color_square_d // 2

        for (cx,cy), color in zip(centers, self.colors):
            x0 = cx - half_d
            y0 = cy - half_d
            for y in range(y0,y0+self.color_square_d):
                for x in range(x0, x0+self.color_square_d):
                    self.backbuffer.put_pixel(x,y,color)
                    pass              
        self.backbuffer.commit()

    def render(self, window_total_h:int):
        x_offset = 0
        y_offset = window_total_h - self.h
        
        glWindowPos2i(x_offset, y_offset)
        glDrawPixels(
            self.w,
            self.h,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            bytes(self.frontbuffer.pixels)
        )