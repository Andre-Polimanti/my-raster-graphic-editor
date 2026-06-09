from .pencil import Pencil
from ..canvas import Canvas

class Eraser(Pencil):
    def __init__(self,canvas:Canvas):
        super().__init__(canvas)
        self.color = (self.canvas.frontbuffer.bg_color)
        
    def set_color(self, _): pass