from lib.DrawPixel import draw_pixel

def draw_line(buffer, x1:int,y1:int, x2:int,y2:int, color:tuple, size:int):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x_incr = 1 if x1 < x2 else -1
    y_incr = 1 if y1 < y2 else -1

    if dx >= dy:
        p = 2 * dy -dx
        while True:
            draw_pixel(buffer, x1,y1, color, size)
            if x1 == x2: break
            
            x1 += x_incr
            if p < 0:
                p += 2 * dy
            else:
                y1 += y_incr
                p += 2 * (dy - dx)
    else:
        p = 2 * dx - dy
        while True:
            draw_pixel(buffer, x1,y1, color, size)
            if y1 == y2: break

            y1 += y_incr
            if p < 0:
                p += 2 * dx
            else:
                x1 += x_incr
                p += 2 * (dx - dy)
