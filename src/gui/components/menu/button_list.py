from OpenGL.GL import *

from core.front_buffer import FrontBuffer
from core.back_buffer import BackBuffer

from .button import Button

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

        # This class contains buttons with drawn shapes used for saving or clearing the Canvas

    def create_buttons(self):
        side = self.w // 2
        center_x = self.w // 2
        
        clear_y = self.current_y
        save_y = self.current_y - side - 60

        # Depending on the function of the button, passed as a string here, the button has a different appearance
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