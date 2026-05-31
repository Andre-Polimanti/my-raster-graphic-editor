def paint(buffer, x: int, y: int, color: tuple, size: int): 
    if size <= 0:
        buffer.put_pixel(x, y, color)
        return
    
    for i in range(-size, size + 1):
        for j in range(-size, size + 1):
            px, py = x + i, y + j
            buffer.put_pixel(px, py, color)