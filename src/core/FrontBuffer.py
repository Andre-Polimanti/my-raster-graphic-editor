class FrontBuffer:
    def __init__(self, width:int, height:int, background_color:tuple = (255,255,255,255)):
        self.w = width
        self.h = height
        self.bg_color = background_color

        r,g,b,a= background_color
        self.pixels = bytearray([r, g, b, a] * (width * height))

    def is_valid_pixel(self, x:int,y:int):
        return (0 <= x < self.w and 0 <= y < self.h)

    def put_pixel(self, x:int,y:int, color:tuple):
        is_valid_operation = self.is_valid_pixel(x,y)
        if is_valid_operation:
            idx = (y * self.w + x) * 4
            self.pixels[idx]     = color[0] # R
            self.pixels[idx + 1] = color[1] # G
            self.pixels[idx + 2] = color[2] # B
            self.pixels[idx + 3] = color[3] # Alpha
            return True
        print(f"Pixel of coordinates ({x},{y}) is invalid!")
        return False

    def get_pixel(self, x:int,y:int):
        is_valid_operation = self.is_valid_pixel(x,y)
        if is_valid_operation:
            idx = (y * self.w + x) * 4
            return (self.pixels[idx], self.pixels[idx+1], self.pixels[idx+2], self.pixels[idx+3])
        #print("Invalid pixel!")
        return self.bg_color
    
    def clear(self):
        r, g, b, a= self.bg_color
        self.pixels[:] = bytearray([r, g, b, a] * (self.w * self.h))
        #print("FrontBuffer cleared!")