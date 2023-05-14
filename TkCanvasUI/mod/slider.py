import math
from tkinter import Label
import cairo
from PIL import Image, ImageTk


def surface_to_image(surface):
    buf = surface.get_data()
    width = surface.get_width()
    height = surface.get_height()
    return Image.frombuffer('RGBA', (width, height), buf, 'raw', 'BGRA', 0, 1)


class Slider:

    def __init__(self, master, min_num=0, max_num=100, step=1, default=0,
                 line_length=200, is_horizontal=True, line_stroke=8, line_color=(0.12, 0.12, 0.13, 0.3),
                 block_radius=20, block_color=(1.00, 1.00, 1.00, 0.7)):
        # self.line = Label(master)
        # self.block = Label(master)
        self.root = Label(master)
        self.min_num = min_num
        self.max_num = max_num
        self.step = step
        self.default = default
        self.value = default
        self.line_length = line_length
        self.is_horizontal = is_horizontal
        self.line_stroke = line_stroke
        self.line_color = line_color
        self.block_radius = block_radius
        self.block_color = block_color
        # self.line_img = None
        # self.block_img = None
        self.img = None
        self.draw()

    def draw_lien(self):
        if self.is_horizontal:
            width, height = self.line_length, self.line_stroke
        else:
            width, height = self.line_stroke, self.line_length
        radius = height / 2
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        cr = cairo.Context(surface)
        cr.set_source_rgba(*self.line_color)
        cr.set_line_width(self.line_stroke)
        cr.arc(radius, radius, radius, math.pi, 3 * math.pi / 2)  # 左上角
        cr.arc(width - radius, radius, radius, 3 * math.pi / 2, 0)  # 右上角
        cr.arc(width - radius, height - radius, radius, 0, math.pi / 2)  # 右下角
        cr.arc(radius, height - radius, radius, math.pi / 2, math.pi)  # 左下角
        cr.close_path()
        cr.fill()
        return surface

    def draw_block(self):
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.block_radius, self.block_radius)
        cr = cairo.Context(surface)
        cr.set_source_rgba(*self.block_color)
        cr.set_line_width(self.block_radius)
        cr.arc(self.block_radius / 2, self.block_radius / 2, self.block_radius / 2, 0, 2 * math.pi)
        cr.close_path()
        cr.fill()
        return surface

    def _draw(self):
        if self.is_horizontal:
            width, height = self.line_length, self.line_stroke
        else:
            width, height = self.line_stroke, self.line_length
        radius = height / 2
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, self.block_radius)
        line_cr = cairo.Context(surface)
        line_cr.translate(0, self.block_radius / 2 - self.line_stroke / 2)
        line_cr.set_source_rgba(*self.line_color)
        line_cr.set_line_width(self.line_stroke)
        line_cr.arc(radius, radius, radius, math.pi, 3 * math.pi / 2)  # 左上角
        line_cr.arc(width - radius, radius, radius, 3 * math.pi / 2, 0)  # 右上角
        line_cr.arc(width - radius, height - radius, radius, 0, math.pi / 2)  # 右下角
        line_cr.arc(radius, height - radius, radius, math.pi / 2, math.pi)  # 左下角
        line_cr.close_path()
        line_cr.fill()
        block_cr = cairo.Context(surface)
        block_cr.set_source_rgba(*self.block_color)
        block_cr.set_line_width(self.block_radius)
        block_cr.arc(self.block_radius / 2, self.block_radius / 2, self.block_radius / 2, 0, 2 * math.pi)
        block_cr.close_path()
        block_cr.fill()
        return surface

    def draw(self):
        # surface_to_image(self._draw()).show()
        self.img = ImageTk.PhotoImage(image=surface_to_image(self._draw()))
        self.root.config(image=self.img)
        # self.line_img = ImageTk.PhotoImage(image=surface_to_image(self.draw_lien()))
        # self.line.config(image=self.line_img)
        # self.block_img = ImageTk.PhotoImage(image=surface_to_image(self.draw_block()))
        # self.block.config(image=self.block_img)

    def pack(self, **kwargs):
        self.root.pack(**kwargs)

    def place(self, **kwargs):
        self.root.place(**kwargs)

    def grid(self, **kwargs):
        self.root.grid(**kwargs)
