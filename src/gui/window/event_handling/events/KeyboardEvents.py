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
                    #print("The key ESC was pressed, Main Window is set to be closed.")
                    glfw.set_window_should_close(window, True)
                case glfw.KEY_Q:
                    self.canvas.clear()

                case glfw.KEY_E:
                    # print("The key E was pressed, the current edit is interrupted.")
                    self.handler.cancel_canvas_edit()

                case glfw.KEY_L:
                    self.handler.set_tool("Line")
                case glfw.KEY_P:
                    self.handler.set_tool("Pencil")
