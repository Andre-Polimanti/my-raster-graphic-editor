from OpenGL.GL import *

from core.front_buffer import FrontBuffer
from core.back_buffer import BackBuffer

class Canvas:
    def __init__(self, width:int,height:int, x_offset:int):
        self.x_offset = x_offset
        self.w = width
        self.h = height

        self.frontbuffer = FrontBuffer(self.w,self.h, (255,255,255,255))
        self.backbuffer = BackBuffer(self.frontbuffer)

        self.is_ahead_of_display = True

    def render(self):
        glWindowPos2i(self.x_offset,0) # On the left, we have the color palette, so we have to put the canvas to the right using an x_offset

        glDrawPixels(
            self.w,
            self.h,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            bytes(self.frontbuffer.pixels)
        )

        self.is_ahead_of_display = False

    def render_edit(self):
        # When the BakcBuffer has something in its dirty_pixels, there is something being drawn, so we use this for showing a Tool/Edit Preview
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        glWindowPos2i(self.x_offset,0)
        glDrawPixels(
            self.w,
            self.h,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            bytes(self.backbuffer.pixels)
        )
        glDisable(GL_BLEND)

    def upload_backbuffer(self):
        self.backbuffer.commit()
        self.is_ahead_of_display = True

    def clear(self):
        self.frontbuffer.clear()
        self.is_ahead_of_display = True

    def current_edit_clear(self):
        self.backbuffer.clear()
        self.is_ahead_of_display = True
        # We can abort an edit without committing it