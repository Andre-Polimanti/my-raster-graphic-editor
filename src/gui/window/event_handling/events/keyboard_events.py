import glfw

class KeyboardEvents:
    def __init__(self, handler):
        self.handler = handler
        self.window = handler.window
        self.canvas = handler.canvas

    def key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            match key:
                case glfw.KEY_ESCAPE:
                    print("The key ESC was pressed, Main Window is set to be closed.")
                    glfw.set_window_should_close(self.window, True)
                case glfw.KEY_Q:
                    print("The key Q was pressed, Canvas is set to be cleared.")
                    self.canvas.clear()
                case glfw.KEY_P:
                    # This one communicates with mouse events, so it must be handled by the orchestrator/handler class
                    print("The key P was pressed, the current edit is interrupted.")
                    self.handler.cancel_canvas_edit()
