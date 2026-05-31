class ColorSquare:
    def __init__(self, x:int,y:int, side:int, color:tuple[int,int,int,int]):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def is_inside(self, px, py):
        return (self.x <= px < self.x + self.side) and (self.y <= py < self.y + self.side)

    def draw(self, buffer):
        for y in range(self.y, self.y + self.side):
            for x in range(self.x, self.x + self.side):
                buffer.put_pixel(x, y, self.color)