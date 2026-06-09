from ...primitives.lines.bresenham import draw_line

def draw_x(buffer, x1:int,y1:int, x2:int,y2:int, color:tuple, size:int):
    draw_line(buffer, x1, y1, x2, y2, color, size)
    draw_line(buffer, x1, y2, x2, y1, color, size)