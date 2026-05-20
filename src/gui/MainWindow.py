import glfw
from OpenGL.GL import *
from gui.components.Canvas import Canvas

class MainWindow:
    def __init__(self, width:int,height:int):
        self.title = 'MiniPaint'
        self.w = width
        self.h = height

        self.canvas = Canvas(width,height)

        if not(glfw.init()):
            print("Failed to star GLFW")
            return
        
        self.window = glfw.create_window(width,height, self.title, None,None)
        if not(self.window):
            print("Failed to create Main Window")
            glfw.terminate()
            return
        
        glfw.set_window_size_limits(self.window, self.w,self.h, 1980,1080)

        glfw.set_cursor_pos_callback(self.window, self.cursor_position_callback)
        glfw.set_mouse_button_callback(self.window, self.mouse_button_callback)
        
        glfw.set_key_callback(self.window, self.key_callback)

        glfw.make_context_current(self.window)
        
        self.is_drawing = False
        self.start_x = 0
        self.start_y = 0

    def cursor_position_callback(self, window, xpos, ypos):
        # Só desenhamos o preview (backbuffer) se o botão estiver pressionado!
        if self.is_drawing:
            # Aqui o senhor chamará o self.canvas.backbuffer.clear()
            # E depois mandará o DDA desenhar a linha do (start_x, start_y) até o (xpos, ypos)
            pass
    
    def mouse_button_callback(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_LEFT:
            if action == glfw.PRESS:
                self.is_drawing = True
                # Pegamos a posição exata onde o usuário clicou para ser a âncora do DDA
                self.start_x, self.start_y = glfw.get_cursor_pos(window)
                self.start_x = int(self.start_x)
                self.start_y = int(self.start_y)
                print(f"Start at: X={self.start_x}, Y={self.start_y}")
                
            elif action == glfw.RELEASE:
                self.is_drawing = False
                # O botão foi solto. Hora do Commit Final!
                # self.canvas.upload_backbuffer()
                print("Mouse button has been released - Commit from BackBuffer on FrontBuffer!")

    def key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            if(key == glfw.KEY_ESCAPE):
                print("The key ESC was pressed, Main Window is set to be closed.")
                glfw.set_window_should_close(window,True)
            elif(key == glfw.KEY_Q):
                print("The key Q was pressed, Canvas is set to be cleared.")
                self.canvas.clear()

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
        print("Main Window closed.\n")



