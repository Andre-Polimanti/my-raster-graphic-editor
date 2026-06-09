from .front_buffer import FrontBuffer

# This buffer is to be used as a temporary layer, where only the current edit is stored, once it's comitted or aborted, this buffer is cleared.
# The pixels that are touched by the current edit will be put above the FrontBuffer, so that the user can see a preview of his work.
class BackBuffer(FrontBuffer):
    def __init__(self, front_buffer:FrontBuffer):    
        super().__init__(front_buffer.w,front_buffer.h, (0,0,0,0)) #It's background color is transparent.
        self.front_buffer = front_buffer

        self.dirty_pixels = set() # Pixels touched by the edit.

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
            self.front_buffer.put_pixel(x,y,color) # The pixels touched by the edit are painted on the FrontBuffer
            
        self.clear()