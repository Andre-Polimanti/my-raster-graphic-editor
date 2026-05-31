from OpenGL.GL import *
from PIL import Image

from gui.components.canvas import Canvas

def export_canvas(canvas:Canvas, filename="src/lib/archives/my_drawing.png"):
    w = canvas.w
    h = canvas.h

    pixels = glReadPixels(canvas.my_x_offset, 0, w,h, GL_RGBA, GL_UNSIGNED_BYTE)
    
    image = Image.frombytes("RGBA", (w,h), pixels)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    
    image.save(filename)
    print(f"Imagem salva com sucesso como: {filename}")