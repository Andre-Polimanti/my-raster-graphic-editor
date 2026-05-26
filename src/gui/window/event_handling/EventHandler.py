import glfw

from gui.components.Canvas import Canvas

from gui.components import Tools
from gui.window.event_handling.events.KeyboardEvents import KeyboardEvents
from gui.window.event_handling.events.MouseEvents import MouseEvents

class EventHandler:
    def __init__(self, window, canvas:Canvas):
        self.window = window

        self.canvas = canvas
        self.is_drawing = False

        self.current_tool:Tools = None
        self.tool_size = 1 

        self.mouse = MouseEvents(self)
        self.keyboard = KeyboardEvents(self)
    
    def cancel_canvas_edit(self):
        if self.mouse.is_drawing:
            self.mouse.stop_drawing()
            self.canvas.current_edit_clear()