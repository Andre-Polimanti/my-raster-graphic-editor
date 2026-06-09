import glfw
from OpenGL.GL import *

from ..components.menu.button_list import ButtonList
from ..components.canvas import Canvas
from ..components.palette.color_palette import ColorPalette

from .event_handling.event_handler import EventHandler

class MainWindow:
    def __init__(self):
        self.title = 'MiniPaint'

        self.palette_section = 180
        self.canvas_section = 1600
        self.menu_section = 140

        self.w = self.palette_section + self.canvas_section + self.menu_section
        self.h = 1080

        self.color_palette = ColorPalette(self.palette_section, self.h, self.palette_section//5*3)
        self.canvas = Canvas(self.canvas_section, self.h, self.palette_section)
        self.button_menu = ButtonList(self.menu_section, self.h)

        if not(glfw.init()):
            print("Failed to start GLFW")
            return
        
        screen = glfw.get_primary_monitor()
        self.window = glfw.create_window(self.w, self.h, self.title, screen, None)

        if not(self.window):
            print("Failed to create Main Window")
            glfw.terminate()
            return
        
        # Event orchestrator
        self.event_handler = EventHandler(self)

        # Mouse events
        glfw.set_cursor_pos_callback(self.window, self.event_handler.mouse.pos_callback)
        glfw.set_mouse_button_callback(self.window, self.event_handler.mouse.button_callback)

        #Keyboard events
        glfw.set_key_callback(self.window, self.event_handler.keyboard.key_callback)
        
        # Window settings
        glfw.set_window_size_limits(self.window, self.w,self.h, self.w,self.h)

        # Commiting all settings
        glfw.make_context_current(self.window)

    def run(self):
        glClearColor(0.2,0.3,0.3,1.0)
            
        while not(glfw.window_should_close(self.window)):
            glfw.poll_events()

            glViewport(0,0, self.w, self.h)
            glClear(GL_COLOR_BUFFER_BIT)

            self.color_palette.render(x_offset=0)
            self.canvas.render()
            self.button_menu.render(x_offset= self.palette_section + self.canvas_section)
            # We render color_palette and button_menu everytime, a problem that will not be solved in this project

            glfw.swap_buffers(self.window)
        glfw.terminate()
        #print("Main Window closed.\n")