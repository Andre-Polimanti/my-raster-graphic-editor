from ...canvas import Canvas

class Tool:
    def __init__(self, canvas:Canvas):
        self.canvas = canvas
        self.color = (0,0,0,255)
        self.size = 0

    def on_press(self, x:int,y:int): pass
    def on_drag(self, x0:int,y0:int, x1:int,y1:int): pass

    def set_size(self, new_size:int):
        self.size = new_size

    def set_color(self, selected_color:tuple):
        if selected_color:
            self.color = selected_color

    def on_release(self):
        self.canvas.upload_backbuffer()

    def switch_is_filled(self):
        pass