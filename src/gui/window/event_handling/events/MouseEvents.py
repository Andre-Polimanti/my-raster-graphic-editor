import glfw

from lib.archives.image import export_canvas

from ....components.ColorPalette import ColorPalette
from ....components.Canvas import Canvas
from ....components.Buttons import ButtonList

class MouseEvents:
    def __init__(self, handler):        
        self.handler = handler
        self.renderer = handler.renderer
        self.window = handler.window

        self.color_palette:ColorPalette = handler.color_palette
        self.canvas: Canvas = handler.canvas
        self.button_menu:ButtonList = handler.button_menu
    
        self.x0 = 0
        self.y0 = 0

        self.is_drawing = False

        self.bound_palette = self.renderer.palette_section
        self.bound_canvas = self.renderer.palette_section + self.renderer.draw_section
        self.bound_buttons = self.bound_canvas + self.renderer.button_section

    def stop_drawing(self):
        self.is_drawing = False

    def normalize_vertical_axis(self, ypos): #It's inverted by default
        return self.renderer.h - int(ypos) - 1
    
    def button_callback(self, window, button, action, mods):        
        if button != glfw.MOUSE_BUTTON_LEFT:
            return
        
        x,y =  glfw.get_cursor_pos(window)
        y = self.normalize_vertical_axis(int(y))

        if x < self.bound_buttons and action == glfw.PRESS:
            local_x = int(x - self.bound_canvas) 
            
            for btn in self.button_menu.buttons:
                if btn.was_clicked(local_x, y):
                    if btn.func == "Clear":
                        self.canvas.clear()
                        #print("Canvas cleared by mouse instruction!")

                    elif btn.func == "Save":
                        export_canvas(self.canvas)
                        #print("Salving image!")

        tool = self.handler.current_tool
        if not tool:
            return

        if self.bound_palette <= x < self.bound_canvas:
            x = int(x - self.bound_palette)
            if action == glfw.PRESS:
                self.is_drawing = True

                self.x0 = x
                self.y0 = y
                tool.on_press(self.x0,self.y0)
            if action == glfw.RELEASE:
                if self.is_drawing:
                    tool.on_release()
                    self.is_drawing = False
        else:
            self.is_drawing = False
            if x < self.bound_palette:
                if action == glfw.PRESS:
                    color = self.color_palette.get_color(x,y)
                    if color:
                        self.handler.current_tool.set_color(color)
                        #print(f"Current color: {color}")

    def pos_callback(self, window, xpos, ypos):
        if not self.is_drawing: 
            return
        
        if self.bound_palette <= xpos < self.bound_canvas:
            tool = self.handler.current_tool
            if tool:            
                x = int(xpos - self.bound_palette)
                y = self.normalize_vertical_axis(int(ypos)) # We only update the current cursor position, since the first one was normalized on the moment the button was pressed
                tool.on_drag(self.x0,self.y0, x,y)
        else:
            self.handler.abort_edit()