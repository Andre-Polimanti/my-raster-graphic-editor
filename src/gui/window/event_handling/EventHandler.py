import glfw

from ...components import Tools

from ...components.Canvas import Canvas
from ...components.ColorPalette import ColorPalette

from .events.KeyboardEvents import KeyboardEvents
from .events.MouseEvents import MouseEvents

class EventHandler:
    def __init__(self, renderer):
        self.renderer = renderer

        self.window = self.renderer.window
        self.canvas:Canvas = self.renderer.canvas
        self.color_palette:ColorPalette = self.renderer.color_palette

        self.is_drawing = False
        self.current_tool:Tools = None        

        self.mouse = MouseEvents(self)
        self.keyboard = KeyboardEvents(self)
    
    def cancel_canvas_edit(self):
        if self.mouse.is_drawing:
            self.mouse.stop_drawing()
            self.canvas.current_edit_clear()