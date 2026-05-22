import glfw

from gui.components.Canvas import Canvas
from lib.primitives.lines.bresenham import draw_line

class MouseEvents:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.window = orchestrator.window
        self.canvas: Canvas = orchestrator.canvas

        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0

        self.current_tool = "Line" # For testing
        self.is_drawing = False
    
    def stop_drawing(self):
        if self.is_drawing:
            self.is_drawing = False

    def normalize_vertical_axis(self, ypos): #It's inverted by default
        h = (glfw.get_window_size(self.window)[1])

        y = int(ypos)
        y = h - y - 1

        return y

    def cursor_pos_callback(self, window, xpos, ypos):
        if not self.is_drawing:
            return
        
        match self.current_tool:
            case None:
                return
            
            case "Line":
                current_x = int(xpos)
                current_y = self.normalize_vertical_axis(ypos)

                self.canvas.current_edit_clear() # Only the starter and ending points will be used for crafting a line, all others can be descarded

                draw_line(self.canvas.backbuffer, self.x0, self.y0, current_x, current_y, (0, 0, 0, 255))

    def button_callback(self, window, button, action, mods):
        match self.current_tool:
            case None:
                return
            
            case "Line":
                if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
                    self.is_drawing = True
                    print(f"Tool: {self.current_tool}")

                    x, y = glfw.get_cursor_pos(window)
                    self.x0, self.y0 = int(x), int(y)
                    self.y0 = self.normalize_vertical_axis(self.y0)

                    print(f"X0={self.x0}, Y0={self.y0}")
        
                if action == glfw.RELEASE:
                    if self.is_drawing:            
                        x, y = glfw.get_cursor_pos(window)
                        self.x1, self.y1 = int(x), int(y)
                        self.y1 = self.normalize_vertical_axis(self.y1)

                        print(f"X1={self.x1}, Y1={self.y1}")

                        draw_line(self.canvas.backbuffer, self.x0,self.y0, self.x1,self.y1, (0, 0, 0, 255))
        
                        self.canvas.upload_backbuffer()

                        self.is_drawing = False