from tkinter import Canvas
from TkCanvasUI2.Collider import Polygon


class BaseWidget:

    def __init__(self):
        self.collisions: list[Polygon] = []

    def redraw(self):
        pass

    def is_collision(self, coord):
        for collision in self.collisions:
            if collision.collider(coord):
                return True

    def button_1_event(self, event):
        pass


class BaseCanvasUI(Canvas):

    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)
        self.bind('<Button-1>', self.button_1_event)
        self.bind('<Configure>', self.draw)
        self.widgets: list[BaseWidget] = []

    def draw(self, event=None):
        for widget in self.widgets:
            widget.redraw()

    def button_1_event(self, event=None):
        widget = self.collision((event.x, event.y))
        if widget is None:
            return
        widget.button_1_event(event)

    def collision(self, coord) -> BaseWidget:
        for widget in self.widgets:
            if widget.is_collision(coord):
                return widget

    def add(self, widget: BaseWidget):
        self.widgets.append(widget)
