import cairo

# 创建Cairo图形设备和绘图上下文
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 200, 200)
cr = cairo.Context(surface)

# 绘制圆
cr.arc(50, 50, 40, 0, 2 * 3.1416)
cr.set_source_rgb(0.8, 0.3, 0.2)
cr.fill()

# 平移整个图形
cr.translate(50, 0)

# 再次绘制圆
cr.arc(50, 50, 40, 0, 2 * 3.1416)
cr.fill()

# 将图形保存到文件
surface.write_to_png("circle.png")
