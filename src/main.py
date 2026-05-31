from OpenGL.GL import *

from gui.window.window import MainWindow

def main():
    app = MainWindow()

    # max_w = w - 1
    # max_h = h - 1

    # draw_line(app.canvas.backbuffer, max_w,max_h, 0,0, (0,0,0,255))
    # draw_line(app.canvas.backbuffer, 0,max_h, max_w,0, (0,0,0,255))
    # app.canvas.upload_backbuffer()

    # draw_line(app.canvas.backbuffer, max_w//2,max_h, max_w//2,0, (0,0,0,255))
    # draw_line(app.canvas.backbuffer, 0,max_h//2, max_w,max_h//2, (0,0,0,255))
    # app.canvas.upload_backbuffer()

    # draw_line(app.canvas.backbuffer, max_w,max_h, 0, max_h//2, (0,0,0,255))
    # draw_line(app.canvas.backbuffer, 0,max_h, max_w,max_h//2, (0,0,0,255))
    # app.canvas.upload_backbuffer()
    
    app.run()
main()