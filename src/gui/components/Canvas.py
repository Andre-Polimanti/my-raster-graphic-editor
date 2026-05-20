from OpenGL.GL import *

from core.Buffer import Buffer
from core.BackBuffer import BackBuffer

class Canvas:
    def __init__(self, width:int,height:int):
        self.w = width
        self.h = height

        self.frontbuffer = Buffer(width,height, (255,255,255,255))
        self.backbuffer = BackBuffer(self.frontbuffer)

        """if(not glfw.init()):    
            print("Failed to start GLFW")
            return

        self.window = glfw.create_window(width, height, "Canvas", None, None)
        if self.window == None:
            print("Failed to create Canvas Window")
            glfw.terminate()

        glfw.make_context_current(self.window) """

    def render(self, w:int,h:int):
        """ w,h = glfw.get_framebuffer_size(self.window)
        glViewport(0,0,w,h) """

        x_offset = (w - self.w) // 2
        y_offset = (h - self.h) // 2

        glWindowPos2i(x_offset,y_offset)
        glDrawPixels(
            self.frontbuffer.w,
            self.frontbuffer.h,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            bytes(self.frontbuffer.pixels)
        )
        """ glfw.swap_buffers(self.window) """

    def upload_backbuffer(self):
        self.backbuffer.commit()

    def clear(self):
        self.backbuffer.clear()
        self.frontbuffer.clear()
        print("Canvas cleared.\n")
