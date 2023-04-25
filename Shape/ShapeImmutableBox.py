try:
    from BaseShape import BaseShape
except ImportError:
    from .BaseShape import BaseShape


def append_shapes(shapes, mod, shape: BaseShape):
    """添加形状检测体(操作符，碰撞函数，是否取反，关键数据)
    :param shapes: 形状检测体的列表
    :param mod: 操作符
    :param shape: 形状检测体"""
    shapes.append((mod, shape.collision_fun, shape.get_key()))


def collision_fun(shapes, point):
    """形状检测体的组合类的碰撞函数

    :param shapes: 形状检测体的列表
    :param point: 坐标
    :return: 返回一个布尔值，表示是否碰撞
    """
    ret = True
    for mod, collision_fun_, key in shapes:
        ret_ = collision_fun_(key, point)
        if mod == "or":
            ret = ret or ret_
        elif mod == "and":
            ret = ret and ret_
        elif mod == "and not":
            ret = ret and not ret_
    return ret


class ShapeBox(BaseShape):
    """形状检测体的组合类"""

    def __init__(self, shape, point=(0, 0), centre=(0, 0), contrary=False):
        """形状检测体的组合类

        :param shape: 一个形状检测体或形状检测体列表
        :param point: 坐标,它是一个包含x和y坐标的元组
        :param centre: 中心点坐标，它是一个包含中心点的x和y坐标的元组
        :param contrary: 一个布尔值，用于确定是否将结果取反。如果它被设置为True，返回值将取反，默认值到False(可选)
        """
        super().__init__(point, centre, contrary)
        self.collision_fun = collision_fun
        if isinstance(shape, list):
            self.shape = shape
        elif issubclass(type(shape), BaseShape):
            self.shape = []
            self.__iadd('and', shape)
        else:
            raise ValueError()

    def __add(self, mod, shape: BaseShape):
        if not isinstance(shape, ShapeBox):
            raise TypeError("The type of shape must be ShapeBox")
        shape_ = self.copy()
        append_shapes(shape_.shape, mod, shape)
        return shape_

    def __iadd(self, mod, shape: BaseShape):
        if not isinstance(shape, ShapeBox):
            raise TypeError("The type of shape must be ShapeBox")
        append_shapes(self.shape, mod, shape)
        return self

    def or_(self, shape):
        return self.__add("or", shape)

    def and_(self, shape):
        return self.__add("and", shape)

    def ior(self, shape):
        return self.__iadd("or", shape)

    def iand(self, shape):
        return self.__iadd("and", shape)

    def __or__(self, shape):
        return self.or_(shape)

    def __and__(self, shape):
        return self.and_(shape)

    def __invert__(self):
        self.contrary = not self.contrary
        return self

    def __add__(self, shape):
        return self.or_(shape)

    def __sub__(self, shape):
        return self.and_(~shape)

    def __mul__(self, shape):
        return self.and_(shape)

    def __iadd__(self, shape):
        return self.ior(shape)

    def __isub__(self, shape):
        return self.iand(~shape)

    def __imul__(self, shape):
        return self.iand(shape)

    def get_key(self):
        return self.contrary, self.shape

    def collision(self, point):
        collision_fun([("and", self.collision_fun, self.get_key())], point)

    def copy(self):
        return ShapeBox(self.shape.copy(), self.point, self.centre, self.contrary)
