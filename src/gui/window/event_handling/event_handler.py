import glfw

from ...components.tools.base.tool import Tool

from ...components.canvas import Canvas
from ...components.palette.color_palette import ColorPalette
from ...components.menu.menu_grid import MenuGrid


from .events.keyboard_events import KeyboardEvents
from .events.mouse_events import MouseEvents

class EventHandler:
    def __init__(self, renderer):
        self.renderer = renderer

        self.window = self.renderer.window
        self.canvas:Canvas = self.renderer.canvas
        self.color_palette:ColorPalette = self.renderer.color_palette
        self.button_menu:MenuGrid = self.renderer.button_menu

        self.is_drawing = False
        self.current_tool:Tool = None      
        self.current_color = (0,0,0,255)

        self.mouse = MouseEvents(self)
        self.keyboard = KeyboardEvents(self)
    
    def set_tool(self, tool:Tool):
        self.current_tool = tool

    def set_tool_size(self, size:int):
        if self.current_tool:
            self.current_tool.set_size(size)
            
    def set_color(self, new_color:tuple):
        self.current_color = new_color

    def abort_edit(self):
        if self.mouse.is_drawing:
            self.mouse.stop_drawing()
            self.canvas.current_edit_clear()