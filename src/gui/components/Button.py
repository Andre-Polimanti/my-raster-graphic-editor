from OpenGL.GL import *
from PIL import Image
import os
from core.FrontBuffer import FrontBuffer

# só precisa adicionar funcionalidade para eles, depois vou colocar e esse PIL é só dar pip install Pillow, ele serve para ler as imagens .png

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, action: str, icon_path: str = None):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.color = color
        self.action = action
        self.icon_path = icon_path

    def is_inside(self, px, py):
        return (self.x <= px < self.x + self.w) and (self.y <= py < self.y + self.h)

    def draw(self, buffer):
        for y in range(self.y, self.y + self.h):
            for x in range(self.x, self.x + self.w):
                buffer.put_pixel(x, y, self.color)

        if self.icon_path:
            try:
                img = Image.open(self.icon_path).convert("RGBA")
                padding = 10
                icon_size = min(self.w, self.h) - (padding * 2)
                img = img.resize((icon_size, icon_size))
                
                offset_x = self.x + (self.w - icon_size) // 2
                offset_y = self.y + (self.h - icon_size) // 2
                
                img_data = img.load()
                for iy in range(icon_size):
                    for ix in range(icon_size):
                        r, g, b, a = img_data[ix, iy]
                        if a > 128: 
                            calc_y = offset_y + (icon_size - 1 - iy)
                            buffer.put_pixel(offset_x + ix, calc_y, (r, g, b, 255))
            except Exception as e:
                print(f"Não foi possível carregar o ícone '{self.icon_path}': {e}")

class ButtonsPanel:
    def __init__(self, width: int, height: int, my_x_offset: int, canvas):
        self.w = width
        self.h = height
        self.my_x_offset = my_x_offset
        self.canvas = canvas
        
        self.frontbuffer = FrontBuffer(self.w, self.h, (80, 80, 80, 255))
        self.buttons = []
        
        self.create_buttons()

    def create_buttons(self):
        button_size = 50
        spacing = 20

        x = (self.w - button_size) // 2
        y1 = self.h - 100
        y2 = y1 - (button_size + spacing)
        y3 = y2 - (button_size + spacing)
        y4 = y3 - (button_size + spacing)
        y5 = y4 - (button_size + spacing)


        directory = os.path.dirname(os.path.abspath(__file__))
        
        folder_images = os.path.join(directory, "..", "..", "Images")
        
        square_directory = os.path.join(folder_images, "square.png")
        circle_directory = os.path.join(folder_images, "circle.png")
        triangle_directory = os.path.join(folder_images, "triangle.png")
        fill_directory = os.path.join(folder_images, "fill-tool.png")
        save_directory = os.path.join(folder_images, "save.png")
        
        btn_square = Button(x, y1, button_size, button_size, (150, 150, 150, 255), "TOOL_SQUARE", square_directory)
        btn_circle = Button(x, y2, button_size, button_size, (150, 150, 150, 255), "TOOL_CIRCLE", circle_directory)
        btn_triangle = Button(x, y3, button_size, button_size, (150, 150, 150, 255), "TOOL_TRIANGLE", triangle_directory)
        btn_fill = Button(x, y4, button_size, button_size, (150, 150, 150, 255), "TOOL_FILL", fill_directory)
        btn_save = Button(x, y5, button_size, button_size, (150, 150, 150, 255), "TOOL_SAVE", save_directory)


        self.buttons.extend([btn_square, btn_circle, btn_fill, btn_triangle, btn_save])
 
        for btn in self.buttons:
            btn.draw(self.frontbuffer)

    def render(self, window_total_h: int):
        y_offset = window_total_h - self.h
        glWindowPos2i(self.my_x_offset, y_offset)
        glDrawPixels(
            self.w, self.h,
            GL_RGBA, GL_UNSIGNED_BYTE,
            bytes(self.frontbuffer.pixels)
        )
