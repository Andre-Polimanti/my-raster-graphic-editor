from .front_buffer import FrontBuffer

# This buffer is to be used as a temporary layer, where only the current edit is stored, once it's comitted or aborted, this buffer is cleared.
# The pixels that are touched by the current edit will be put above the FrontBuffer, so that the user can see a preview of his work.
class BackBuffer(FrontBuffer):
    def __init__(self, front_buffer:FrontBuffer):    
        super().__init__(front_buffer.w,front_buffer.h, (0,0,0,0)) #It's background color is transparent.
        self.front_buffer = front_buffer

        self.dirty_pixels = set() # Pixels touched by the edit.
    
    def clear(self):
        r, g, b, a = self.bg_color
        pixels = self.pixels
        
        w = self.w

        for x, y in self.dirty_pixels:
            idx = ((y * w) + x) * 4
            pixels[idx]     = r
            pixels[idx + 1] = g
            pixels[idx + 2] = b
            pixels[idx + 3] = a

        self.dirty_pixels.clear()

        #print("BackBuffer cleared!")
    
    def commit(self):
        front_buffer_px = self.front_buffer.pixels

        pixels = self.pixels
        w = self.w

        for x,y in self.dirty_pixels:
            idx = ((y * w) + x) * 4
            front_buffer_px[idx]     = pixels[idx]
            front_buffer_px[idx + 1] = pixels[idx + 1]
            front_buffer_px[idx + 2] = pixels[idx + 2]
            front_buffer_px[idx + 3] = pixels[idx + 3]
            
        self.clear()