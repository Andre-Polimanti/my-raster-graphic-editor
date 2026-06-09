import math

from ....draw_pixel import paint

def draw_circle(buffer, x0:int,y0:int, x1:int,y1:int, color:tuple, size:int):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    r = math.isqrt((dx * dx) + (dy * dy)) 
    # Pythagorean theorem for finding the circle radius
        
    if r == 0:
        paint(buffer, x1, y1, color, size)
        return
    
    x = 0
    y = r

    # Midpoint Circle Algorithm from Bresenham
    d = 3 - 2 * r

    while x <= y:
        _draw_circle_points(buffer, x0, y0, x, y, color, size)
        
        if d <= 0:
            d = d + 4 * x + 6
        else:

            d = d + 4 * (x - y) + 10
            y -= 1
            
        x += 1

def _draw_circle_points(buffer, cx, cy, px, py, color, size): # Octant equivalence.
    paint(buffer, cx + px, cy + py, color, size)
    paint(buffer, cx - px, cy + py, color, size)
    paint(buffer, cx + px, cy - py, color, size)
    paint(buffer, cx - px, cy - py, color, size)
    paint(buffer, cx + py, cy + px, color, size)
    paint(buffer, cx - py, cy + px, color, size)
    paint(buffer, cx + py, cy - px, color, size)
    paint(buffer, cx - py, cy - px, color, size)