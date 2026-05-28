from ..primitives.lines.bresenham import draw_line

def draw_rectangle(buffer, x0:int,y0:int, x1:int,y1:int, color:tuple, size:int):
    draw_line(buffer, x0,y0, x0,y1, color,size)
    draw_line(buffer, x0,y0, x1,y0, color,size)

    draw_line(buffer, x1,y1, x1,y0, color,size)
    draw_line(buffer, x1,y1, x0,y1, color,size)