from OpenGL.GL import *
from PIL import Image

from gui.components.canvas import Canvas

def export_canvas(canvas:Canvas, filename="src/archiving/my_drawing.png"):
    pixels = glReadPixels(
        canvas.my_x_offset,
        0,
        canvas.w,
        canvas.h,
        GL_RGBA, GL_UNSIGNED_BYTE
    )
    # pixels now is a 1D array containing all canvas data
    
    image = Image.frombytes("RGBA", (canvas.w,canvas.h), pixels)
    # image now is a 2D array containing all pixels/canvas data, but it's vertically inverted

    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    # image now is canvas
    
    image.save(filename)
    print(f"Image saved as: {filename}")