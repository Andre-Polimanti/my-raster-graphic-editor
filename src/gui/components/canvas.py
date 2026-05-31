from OpenGL.GL import *

from core.front_buffer import FrontBuffer
from core.back_buffer import BackBuffer

class Canvas:
    def __init__(self, width:int,height:int, my_x_offset:int):
        self.my_x_offset = my_x_offset
        self.w = width
        self.h = height

        self.frontbuffer = FrontBuffer(self.w,self.h, (255,255,255,255))
        self.backbuffer = BackBuffer(self.frontbuffer)

    def render(self, w:int,h:int):
        x_offset = self.my_x_offset
        y_offset = (h - self.h) // 2

        glWindowPos2i(x_offset,y_offset)
        glDrawPixels(
            self.frontbuffer.w,
            self.frontbuffer.h,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            bytes(self.frontbuffer.pixels)
        )
        # When drawing, there will be dirty_pixel from BackBuffer, and, as we want to view a preview of the used tool, we must render the them, the background color of the backbuffer is transparent so we render it over the frontbuffer
        if len(self.backbuffer.dirty_pixels):
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            
            glWindowPos2i(x_offset, y_offset)
            glDrawPixels(
                self.backbuffer.w,
                self.backbuffer.h,
                GL_RGBA,
                GL_UNSIGNED_BYTE,
                bytes(self.backbuffer.pixels)
            )
            glDisable(GL_BLEND)

    def upload_backbuffer(self):
        self.backbuffer.commit()

    def clear(self):
        self.frontbuffer.clear()

    def current_edit_clear(self):
        self.backbuffer.clear()