class FrontBuffer:
    def __init__(self, width:int, height:int, background_color:tuple = (255,255,255,255)):
        self.w = width
        self.h = height
        self.bg_color = background_color

        r,g,b,a= background_color
        self.pixels = bytearray([r, g, b, a] * (width * height)) # glDrawPixel, the function used for actual painting, only works with 1D arrays, so we have to make sure this is the format we are working with

    def is_valid_pixel(self, x:int,y:int):
        return (0 <= x < self.w and 0 <= y < self.h)
    
    # Since we are working with a 1D array, we have to adapt our memory accessing methods.
    # (y * self.w) -> jumps the image lines that are anterior to the pixel we want to access
    # ((y * self.w) + x) -> on the line of the wanted pixel, we go to its column
    # ((y * self.w) + x) * 4 -> our pixels have four bytes of colour, so we have to multiply it.
    def put_pixel(self, x:int,y:int, color:tuple):
        if self.is_valid_pixel(x,y):
            idx = ((y * self.w) + x) * 4
            self.pixels[idx]     = color[0] # R
            self.pixels[idx + 1] = color[1] # G
            self.pixels[idx + 2] = color[2] # B
            self.pixels[idx + 3] = color[3] # Alpha
            return True
        else:
            # print(f"Pixel of coordinates ({x},{y}) is invalid!")
            return False

    def get_pixel(self, x:int,y:int):
        if self.is_valid_pixel(x,y):
            idx = ((y * self.w) + x) * 4
            return (self.pixels[idx], self.pixels[idx+1], self.pixels[idx+2], self.pixels[idx+3])
        
        #print("Invalid pixel!")
        return self.bg_color
    
    def clear(self):
        r, g, b, a= self.bg_color
        self.pixels[:] = bytearray([r, g, b, a] * (self.w * self.h))

        #print("FrontBuffer cleared!")