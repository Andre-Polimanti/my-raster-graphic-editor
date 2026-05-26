from __future__ import annotations
import glfw

from typing import Callable

from gui.components.Canvas import Canvas

from gui.components.Tools import Pencil, Line

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

@register_tool(glfw.KEY_E)
def abort_edit(events: KeyboardInterrupt) -> None:
    events.handler.cancel_canvas_edit()

@register_tool(glfw.KEY_Q)
def clear_canvas(events: KeyboardEvents) -> None:
    events.canvas.clear()


@register_tool(glfw.KEY_L)
def set_line_tool(events:KeyboardEvents) -> None:
    line_size = events.tool_size
    events.handler.current_tool = Line(line_size)

@register_tool(glfw.KEY_P)
def set_pencil_tool(events:KeyboardEvents) -> None:
    pencil_size = events.tool_size
    events.handler.current_tool = Pencil(pencil_size)


class KeyboardEvents:
    def __init__(self, handler):
        self.handler = handler

        self.window = handler.window
        self.canvas:Canvas = handler.canvas

        self.tool_size = handler.tool_size

    def key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            key_tool_map.get(key, lambda _: None)(self)    
