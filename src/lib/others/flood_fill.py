from ..draw_pixel import draw_pixel

def flood_fill(buffer, x:int,y:int, color:tuple):
    color_to_change = buffer.get_pixel(x,y)

    if color == color_to_change: return

    pixels_to_go = [(x,y)]

    while len(pixels_to_go) > 0:
        x1,y1 = pixels_to_go.pop()

        current_color = buffer.get_pixel(x1,y1)

        if current_color == color_to_change:
            draw_pixel(buffer, x1,y1, color, 0)

            pixels_to_go.append((x1 + 1, y1))
            pixels_to_go.append((x1 - 1, y1))
            pixels_to_go.append((x1, y1 + 1))
            pixels_to_go.append((x1, y1 - 1))