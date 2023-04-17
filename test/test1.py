from os import chdir
from os.path import split

from TkCanvasUI2.Collider import polygon
from TkCanvasUI2.TkCanvasUI import BaseCanvasUI
import tkinter as tk


class Button(BaseCanvasUI.BaseWidget):

    def __init__(self, canvas: BaseCanvasUI.BaseCanvasUI, x, y, width, height, text, command):
        super().__init__()
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.command = command
        self.collisions.append(polygon.Polygon((0, 0), (width, 0), (width, height), (0, height), point=(x, y)))
        self.rectangle = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                 fill='#ffffff')
        self.text = canvas.create_text(self.x + self.width / 2, self.y + self.height / 2, text=self.text)
        self.canvas.add(self)

    def button_1_event(self, event):
        self.x += 10
        self.y += 10
        self.collisions[0].move(self.x, self.y)
        self.canvas.coords(self.rectangle, self.x, self.y, self.x + self.width, self.y + self.height)
        self.canvas.coords(self.text, self.x + self.width / 2, self.y + self.height / 2)


def main():
    win = tk.Tk()
    canvas = BaseCanvasUI.BaseCanvasUI(win)
    canvas.pack()
    button = Button(canvas, 10, 10, 100, 100, 'button', None)
    win.mainloop()


if __name__ == '__main__':
    chdir(split(__file__)[0])
    main()
