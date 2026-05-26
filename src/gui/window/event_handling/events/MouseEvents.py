import glfw

from gui.components.Canvas import Canvas

class MouseEvents:
    def __init__(self, handler):
        self.handler = handler
        self.window = handler.window
        self.canvas: Canvas = handler.canvas

        self.x0 = 0
        self.y0 = 0

        self.is_drawing = False
    
    def stop_drawing(self):
        self.is_drawing = False

    def normalize_vertical_axis(self, ypos): #It's inverted by default
        h = (glfw.get_window_size(self.window)[1])
        return h - int(ypos) - 1
    
    def button_callback(self, window, button, action, mods):
        tool = self.handler.current_tool

        if not tool or button != glfw.MOUSE_BUTTON_LEFT:
            return
        
        x,y =  glfw.get_cursor_pos(window)

        x = int(x)
        y = self.normalize_vertical_axis(int(y))

        if action == glfw.PRESS:
            self.is_drawing = True

            self.x0 = x
            self.y0 = y
            tool.on_press(self.x0,self.y0)

        if action == glfw.RELEASE:
            if self.is_drawing:
                tool.on_release()
                self.is_drawing = False

    def pos_callback(self, window, xpos, ypos):
        tool = self.handler.current_tool

        if not self.is_drawing: return            
        
        x = int(xpos)
        y = self.normalize_vertical_axis(int(ypos)) # We only update the current cursor position, since the first one was normalized on the moment the button was pressed

        tool.on_drag(self.x0,self.y0, x,y)