import glfw
from OpenGL.GL import *

from ..components.palette.color_palette import ColorPalette
from ..components.canvas import Canvas
from ..components.menu.menu_grid import MenuGrid

from ..window.event_handling.event_handler import EventHandler

class MainWindow:
    def __init__(self):
        self.title = "MiniPaint"

        if not(glfw.init()):
            print("Failed to start GLFW")
            return
        
        screen = glfw.get_primary_monitor()
        mode = glfw.get_video_mode(screen)

        self.w, self.h = mode.size
        self.window = glfw.create_window(self.w, self.h, self.title, screen, None)

        if not(self.window):
            print("Failed to create Main Window")
            glfw.terminate()
            return
        
        glfw.make_context_current(self.window)
                
        self.palette_width = self.w // 10
        self.menu_width = self.w // 12
        self.canvas_width = self.w - self.palette_width - self.menu_width

        self.color_palette = ColorPalette(self.palette_width, self.h, self.palette_width//5*3)
        self.canvas = Canvas(self.canvas_width, self.h, self.palette_width)
        self.button_menu = MenuGrid(self.menu_width, self.h)
        
        # Event orchestrator
        self.event_handler = EventHandler(self)

        # Mouse events
        glfw.set_cursor_pos_callback(self.window, self.event_handler.mouse.pos_callback)
        glfw.set_mouse_button_callback(self.window, self.event_handler.mouse.button_callback)

        #Keyboard events
        glfw.set_key_callback(self.window, self.event_handler.keyboard.key_callback)
        
    def run(self):
        image:Canvas = self.canvas

        glViewport(0, 0, self.w, self.h)
        glClearColor(0.2, 0.3, 0.3, 1.0)

        # ColorPalette and MenuGrid are static so we can render them on the begining and never again
        for _ in range(2):
            glClear(GL_COLOR_BUFFER_BIT)

            self.color_palette.render(x_offset=0)
            image.render()
            self.button_menu.render(x_offset=self.palette_width + self.canvas_width)

            glfw.swap_buffers(self.window)


        # So that we can rerender only the image and its editing, we have to use GL_SCISSOR_TEST, so that we can cut only the part of the display that we wish to work now
        glEnable(GL_SCISSOR_TEST)

        while not(glfw.window_should_close(self.window)):
            glfw.poll_events()

            glScissor(self.palette_width, 0, self.canvas_width, self.h)
            glViewport(self.palette_width, 0, self.canvas_width, self.h)

            must_render_image = image.is_ahead_of_display
            must_render_edit = len(image.backbuffer.dirty_pixels) > 0

            if must_render_image or must_render_edit:
                glClear(GL_COLOR_BUFFER_BIT)
                image.render()
                if must_render_edit:
                    image.render_edit()
                
                glfw.swap_buffers(self.window)

        glfw.terminate()
        #print("Main Window closed.\n")