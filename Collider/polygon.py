from itertools import combinations


class Vector:
    """二维向量"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __mul__(self, v):
        return self.x * v.x + self.y * v.y

    def cross(self, v):
        return self.x * v.y - v.x * self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def points_to_lines(points):
    """ 将点列表转为线段列表

    :param points: 点列表
    :return: 线段列表
    """
    return [(points[i], points[(i + 1) % len(points)])
            for i in range(len(points))]


def is_cross(l1, l2):
    """ 判断两条线段是否相交

    :param l1: 线段1
    :param l2: 线段2
    :return: 两条线段是否相交
    """
    p1, p2 = l1
    p3, p4 = l2
    p1, p2, p3, p4 = Vector(*p1), Vector(*p2), Vector(*p3), Vector(*p4)
    o1, o2 = (p3 - p1).cross(p2 - p1), (p4 - p1).cross(p2 - p1)
    o3, o4 = (p1 - p3).cross(p4 - p3), (p2 - p3).cross(p4 - p3)
    return o1 * o2 < 0 and o3 * o4 < 0


def is_crossing(lines):
    """ 判断多边形是否交叉

    :param lines: 多边形边线
    :return: 多边形是否交叉
    """
    for l1, l2 in combinations(lines, 2):
        if is_cross(l1, l2):
            return True
    return False


def is_crossing_error(lines):
    """ 判断多边形是否交叉,如果交叉则抛出错误

    :param lines: 多边形边线
    """
    if is_crossing(lines):
        raise ValueError('Polygons cannot cross')


def is_ray_intersects_segment(p, a, b):
    """ 判断射线是否与线段相交

    :param p: 射线起点
    :param a: 线段起点
    :param b: 线段终点
    :return: 射线是否与线段相交
    """
    if a[1] > b[1]:
        a, b = b, a
    if p[1] == a[1] or p[1] == b[1]:
        p = (p[0], p[1] + 0.1)
    if p[1] < a[1] or p[1] > b[1] or p[0] > max(a[0], b[0]):
        return False
    if p[0] < min(a[0], b[0]):
        return True
    return (p[0] - a[0]) / (p[1] - a[1]) >= (b[0] - a[0]) / (b[1] - a[1])


def in_polygon(point, lines):
    """ 判断点是否在多边形内部

    :param point: 点坐标
    :param lines: 多边形边线
    :return: 点是否在多边形内部
    """
    is_crossing_error(lines)
    n = 0
    for line in lines:
        if is_ray_intersects_segment(point, line[0], line[1]):
            n += 1
    return n % 2 == 1


def get_mbr(lines):
    """ 获取多边形的最小外接矩形

    :param lines: 多边形边线
    :return: 最小外接矩形
    """
    x_min, x_max = float('inf'), -float('inf')
    y_min, y_max = float('inf'), -float('inf')
    for line in lines:
        for point in line:
            x_min = min(x_min, point[0])
            x_max = max(x_max, point[0])
            y_min = min(y_min, point[1])
            y_max = max(y_max, point[1])
    return x_min, y_min, x_max, y_max


class List(list):
    """一个自动调用函数的列表"""

    def __init__(self, func, *args, **kwargs):
        """ 一个自动调用函数的列表

        :param func: 调用的函数
        :param args: 传入的参数
        :param kwargs: 传入的参数
        """
        super().__init__(*args, **kwargs)
        self.func_end = func

    def __getattribute__(self, item):
        func = super().__getattribute__(item)
        func_end = super().__getattribute__('func_end')

        def func_(*args, **kwargs):
            n = func(*args, **kwargs)
            func_end(self)
            return n

        return func_


def _set_lines(instance):
    instance._lines = points_to_lines(instance.points)
    is_crossing_error(instance._lines)
    instance.mbr = get_mbr(instance._lines)


class Points:
    """多边形的点列表"""

    def __get__(self, instance, owner):
        if not hasattr(instance, '_points'):
            def set_lines(self_):
                _set_lines(instance)
            instance._points = List(set_lines)
        return instance._points

    def __set__(self, instance, value):
        def set_lines(self_):
            _set_lines(instance)
        instance._points = List(set_lines, value)
        _set_lines(instance)


class Lines:
    """多边形的边线列表"""

    def __get__(self, instance, owner):
        if not hasattr(instance, '_lines'):
            instance._lines = None
        return instance._lines

    def __set__(self, instance, value):
        raise AttributeError('can\'t set Lines')


class Polygon:
    """多边形碰撞类"""

    points: List = Points()
    lines: List = Lines()
    mbr = None

    def __init__(self, *points, point, opposite=False):
        """ 多边形碰撞类
        :param points: 其他点的坐标
        :param point: 多边形的坐标
        :param opposite: 判断点是否在多边形内部时是否取反
        """
        self.points = points
        self.point = point
        self.opposite = opposite

    def __str__(self):
        return f"Polygon({self.points})"

    def collider(self, point):
        """ 判断点是否在多边形内部

        :param point: 点坐标
        :return: 点是否在多边形内部
        """
        x = point[0] - self.point[0]
        y = point[1] - self.point[1]
        return ((self.mbr[0] < x < self.mbr[2]) ^ self.opposite and
                (self.mbr[1] < y < self.mbr[3]) ^ self.opposite and
                in_polygon((x, y), self.lines) ^ self.opposite)

    def move(self, x, y):
        self.point = (x, y)
