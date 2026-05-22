import glfw

class KeyboardEvents:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.window = orchestrator.window
        self.canvas = orchestrator.canvas

    def key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            match key:
                case glfw.KEY_ESCAPE:
                    #print("The key ESC was pressed, Main Window is set to be closed.")
                    glfw.set_window_should_close(self.window, True)
                case glfw.KEY_Q:
                    self.canvas.clear()

                case glfw.KEY_E:
                    #print("The key E was pressed, the current edit is interrupted.")
                    self.orchestrator.cancel_canvas_edit()

                case glfw.KEY_L:
                    self.orchestrator.set_tool("Line")
                case glfw.KEY_P:
                    self.orchestrator.set_tool("Pencil")
