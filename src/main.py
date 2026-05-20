from OpenGL.GL import *

from gui.MainWindow import MainWindow
from lib.primitives.lines.dda import draw_line

def main():
    w = 800
    h = 600
    app = MainWindow(w,h)

    draw_line(app.canvas.backbuffer, 0,h//2, w-1,h//2, (0,0,0,255))
    app.canvas.upload_backbuffer()
    draw_line(app.canvas.backbuffer, w//2,0, w//2,h-1,(0,0,0,255))
    app.canvas.upload_backbuffer()

    app.run()

main()