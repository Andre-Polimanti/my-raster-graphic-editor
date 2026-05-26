import glfw

from gui.components.Canvas import Canvas

from gui.components import Tools
from gui.window.event_handling.events.KeyboardEvents import KeyboardEvents
from gui.window.event_handling.events.MouseEvents import MouseEvents

class EventHandler:
    def __init__(self, renderer):
        self.renderer = renderer

        self.window = self.renderer.window
        self.canvas = self.renderer.canvas
        self.color_palette = self.renderer.color_palette

        self.is_drawing = False
        self.current_tool:Tools = None        

        self.mouse = MouseEvents(self)
        self.keyboard = KeyboardEvents(self)
    
    def cancel_canvas_edit(self):
        if self.mouse.is_drawing:
            self.mouse.stop_drawing()
            self.canvas.current_edit_clear()