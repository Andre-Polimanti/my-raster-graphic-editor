from ..draw_pixel import draw_pixel

def draw_circle(buffer, x0:int,y0:int, x1:int,y1:int, color:tuple, size:int):
    # Calcula a distância ao quadrado (Teorema de Pitágoras sem a raiz)
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    r2 = (dx * dx) + (dy * dy)
    
    r = 0
    while (r + 1) * (r + 1) <= r2:
        r += 1
        
    if r == 0:
        draw_pixel(buffer, x1, y1, color, size)
        return

    x = 0
    y = r
    d = 3 - 2 * r 
    
    def draw_circle_points(cx, cy, px, py):
        draw_pixel(buffer, cx + px, cy + py, color, size)
        draw_pixel(buffer, cx - px, cy + py, color, size)
        draw_pixel(buffer, cx + px, cy - py, color, size)
        draw_pixel(buffer, cx - px, cy - py, color, size)
        draw_pixel(buffer, cx + py, cy + px, color, size)
        draw_pixel(buffer, cx - py, cy + px, color, size)
        draw_pixel(buffer, cx + py, cy - px, color, size)
        draw_pixel(buffer, cx - py, cy - px, color, size)

    while x <= y:
        draw_circle_points(x0, y0, x, y)
        
        if d <= 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
            
        x += 1