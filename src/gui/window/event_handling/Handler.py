import glfw

from gui.components.Canvas import Canvas

from gui.window.event_handling.events.keyboard_events import KeyboardEvents
from gui.window.event_handling.events.mouse_events import MouseEvents

from lib.primitives.lines.bresenham import draw_line

class EventHandler:
    def __init__(self, window, canvas:Canvas):
        self.window = window
        self.canvas = canvas

        self.mouse_events = MouseEvents(self)
        self.keyboard_events = KeyboardEvents(self)

        self.is_drawing = False
    
    def cancel_canvas_edit(self):
        if self.mouse_events.is_drawing:
            self.mouse_events.stop_drawing()
            self.canvas.current_edit_clear()