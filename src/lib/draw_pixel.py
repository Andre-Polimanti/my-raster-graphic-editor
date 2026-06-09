def paint(buffer, x: int, y: int, color: tuple, size: int): 
    if size <= 0:
        return

    offset = size // 2
    
    w = buffer.w
    pixels = buffer.pixels
    
    has_dirty_set = hasattr(buffer, 'dirty_pixels')
    if has_dirty_set:
        dirty = buffer.dirty_pixels
        
    r, g, b, a = color

    min_x = max(0, x - offset)
    max_x = min(buffer.w, x + size - offset)
    
    min_y = max(0, y - offset)
    max_y = min(buffer.h, y + size - offset)

    for y in range(min_y, max_y):
        row_base = y * w
        
        for x in range(min_x, max_x):
            idx = (row_base + x) * 4
            
            pixels[idx]     = r
            pixels[idx + 1] = g
            pixels[idx + 2] = b
            pixels[idx + 3] = a
            
            if has_dirty_set:
                dirty.add((x, y))