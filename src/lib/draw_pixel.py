def draw_pixel(buffer, x: int, y: int, color: tuple, size:int): #size is for dimentioning the tool
    if size == 0:
        buffer.put_pixel(x,y, color)
    
    for i in range(-size, size+1):
        for j in range(-size, size+1):
            buffer.put_pixel(x + i, y + j, color)
