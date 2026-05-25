import glfw
from OpenGL.GL import *
from gui.components.Canvas import Canvas

from gui.window.event_handling.EventHandler import EventHandler

class MainWindow:
    def __init__(self, width:int,height:int):
        self.title = 'MiniPaint'
        self.w = width
        self.h = height

        self.canvas = Canvas(width,height)

        if not(glfw.init()):
            print("Failed to start GLFW")
            return
        
        self.window = glfw.create_window(width,height, self.title, None,None)
        if not(self.window):
            print("Failed to create Main Window")
            glfw.terminate()
            return
        
        # Event orchestrator
        self.event_handler = EventHandler(self.window, self.canvas)

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

            current_w,current_h = glfw.get_framebuffer_size(self.window)
            glViewport(0,0, current_w,current_h)
            glClear(GL_COLOR_BUFFER_BIT)

            self.canvas.render(current_w,current_h)

            glfw.swap_buffers(self.window)
        glfw.terminate()
        #print("Main Window closed.\n")