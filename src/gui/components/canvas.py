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

    def render(self):
        glWindowPos2i(self.x_offset,0) # On the left, we have the color palette, so we have to put the canvas to the right using an x_offset

        glDrawPixels(
            self.frontbuffer.w,
            self.frontbuffer.h,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            bytes(self.frontbuffer.pixels)
        )
        # We continuously use the FrontBuffer for re-rendering, which is a problem. One that will not be solved in this project.

        if len(self.backbuffer.dirty_pixels):
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            
            glWindowPos2i(self.x_offset,0)
            glDrawPixels(
                self.backbuffer.w,
                self.backbuffer.h,
                GL_RGBA,
                GL_UNSIGNED_BYTE,
                bytes(self.backbuffer.pixels)
            )
            glDisable(GL_BLEND)
        # When the BakcBuffer has something in its dirty_pixels, there is something being drawn, so we use this for showing a Tool/Edit Preview

    def upload_backbuffer(self):
        self.backbuffer.commit()

    def clear(self):
        self.frontbuffer.clear()

    def current_edit_clear(self):
        self.backbuffer.clear()
        # We can abort an edit without committing it