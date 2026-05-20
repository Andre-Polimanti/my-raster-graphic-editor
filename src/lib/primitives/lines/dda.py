def draw_line(buffer, x1:int,y1:int, x2:int,y2:int, color:tuple):
    dx = x2-x1
    dy = y2-y1
    
    steps = max(abs(dx), abs(dy))

    if(steps==0):
        buffer.put_pixel(x1,y1, color)
        return

    x_incr = dx/steps
    y_incr = dy/steps

    x = float(x1)
    y = float(y1)

    for i in range(steps+1):
        buffer.put_pixel(round(x),round(y), color)
        x += x_incr
        y += y_incr

def get_line(x1:int,y1:int, x2:int, y2:int):
    dx = x2-x1
    dy = y2-y1
    
    steps = max(abs(dx), abs(dy))

    if(steps==0):
        pixel = (x1,y1)
        yield pixel
        return

    x_incr = dx/steps
    y_incr = dy/steps

    x = float(x1)
    y = float(y1)

    for i in range(steps+1):
        pixel = (round(x), round(y))
        yield pixel
        x += x_incr
        y += y_incr