from .front_buffer import FrontBuffer

class BackBuffer(FrontBuffer):
    def __init__(self, front_buffer:FrontBuffer):    
        super().__init__(front_buffer.w,front_buffer.h, (0,0,0,0))

        self.front_buffer = front_buffer
        self.dirty_pixels = set()

    def put_pixel(self, x:int, y:int, color:tuple):
        if super().put_pixel(x,y, color):
            self.dirty_pixels.add((x,y))

    def get_dirty_pixels(self):
        return self.dirty_pixels
    
    def clear(self):
        for x, y in self.dirty_pixels:
            super().put_pixel(x, y, self.bg_color)
        self.dirty_pixels.clear()
        #print("BackBuffer cleared!")
    
    def commit(self):
        for x,y in self.get_dirty_pixels():
            color = self.get_pixel(x,y)
            self.front_buffer.put_pixel(x,y,color)
        self.clear()