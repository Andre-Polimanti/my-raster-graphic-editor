from lib.others.shapes.circle.centered import draw_circle
from lib.others.shapes.rectangle.bresenham import draw_rectangle

from lib.others.shapes.sub_set import draw_x

class Button:
    def __init__(self, x:int, y:int, side:int, func):
        self.x = x
        self.y = y

        self.side = side
        self.func = func

        self.mid_point = self.side//2

    def was_clicked(self, px:int,py:int):
        return (self.x - self.mid_point <= px <= self.x + self.mid_point) and (self.y - self.mid_point <= py <= self.y + self.mid_point)
    
    def draw(self, buffer):
        x0 = self.x - self.mid_point
        y0 = self.y + self.mid_point

        x1 = self.x + self.mid_point
        y1 = self.y - self.mid_point

        draw_rectangle(buffer, x0,y0, x1,y1, (0,0,0,255), 0)
        
        if(self.func == "Clear"): # The button used for clearing the Canvas has a red x in it
            pad = 10
            draw_x(buffer, x0+pad,y0-pad, x1-pad,y1+pad, (255,0,0,255), 1)

        elif(self.func == "Save"): # The button used for saving the canvas has a green circle in it
            r = self.mid_point
            pad = 5
            draw_circle(buffer, self.x, self.y, (self.x + r)-pad, self.y+pad, (0,255,0,255), 1)
