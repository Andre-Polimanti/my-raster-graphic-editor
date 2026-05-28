from __future__ import annotations

import glfw

from typing import Callable


from ....components.Canvas import Canvas
from ....components.Tools import Circle, Rectangle, Eraser, Pencil, Line


type ToolCallback = Callable[[KeyboardEvents], None]

key_tool_map: dict[int, ToolCallback] = {}

def register_tool(key: int) -> Callable[[int], Callable[[ToolCallback], ToolCallback]]:
    def wrapper(callback: ToolCallback) -> ToolCallback:
        key_tool_map[key] = callback
        return callback
    return wrapper

@register_tool(glfw.KEY_ESCAPE)
def close_window(events: KeyboardEvents) -> None:
    glfw.set_window_should_close(events.window, True)

@register_tool(glfw.KEY_A)
def abort_edit(events: KeyboardInterrupt) -> None:
    events.handler.abort_edit()

@register_tool(glfw.KEY_Q)
def clear_canvas(events: KeyboardEvents) -> None:
    events.canvas.clear()


@register_tool(glfw.KEY_L)
def set_line_tool(events:KeyboardEvents) -> None:
    events.handler.current_tool = Line(events.canvas)

@register_tool(glfw.KEY_P)
def set_pencil_tool(events:KeyboardEvents) -> None:
    events.handler.current_tool = Pencil(events.canvas)

@register_tool(glfw.KEY_E)
def set_eraser_tool(events:KeyboardEvents) -> None:
    events.handler.current_tool = Eraser(events.canvas)

@register_tool(glfw.KEY_C)
def set_circle_tool(events:KeyboardEvents) -> None:
    events.handler.current_tool = Circle(events.canvas)

@register_tool(glfw.KEY_R)
def set_rectangle_tool(events:KeyboardEvents) -> None:
    events.handler.current_tool = Rectangle(events.canvas)

@register_tool(glfw.KEY_1)
def set_line_tool(events:KeyboardEvents) -> None:
    events.handler.set_tool_size(0)

@register_tool(glfw.KEY_2)
def set_line_tool(events:KeyboardEvents) -> None:
    events.handler.set_tool_size(1)

@register_tool(glfw.KEY_3)
def set_pencil_tool(events:KeyboardEvents) -> None:
    events.handler.set_tool_size(2)


class KeyboardEvents:
    def __init__(self, handler):
        self.handler = handler

        self.window = handler.window
        self.canvas:Canvas = handler.canvas

    def key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            key_tool_map.get(key, lambda _: None)(self)    
