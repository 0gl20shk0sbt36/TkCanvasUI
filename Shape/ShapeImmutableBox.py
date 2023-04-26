try:
    from ShapeBoxBase import ShapeBoxBase
except ImportError:
    from .ShapeBoxBase import ShapeBoxBase


def collision_fun(key, point):
    """形状检测体的组合类的碰撞函数

    :param shapes: 形状检测体的列表
    :param point: 坐标
    :return: 返回一个布尔值，表示是否碰撞
    """
    contrary, shapes = key
    ret = True
    for mod, collision_fun_, key in shapes:
        ret_ = collision_fun_(key, point)
        if mod == "or":
            ret = ret or ret_
        elif mod == "and":
            ret = ret and ret_
        elif mod == "and not":
            ret = ret and not ret_
    return ret ^ contrary


class ShapeImmutableBox(ShapeBoxBase):
    """形状检测体的组合类"""

    def __init__(self, shape, point=(0, 0), contrary=False):
        """形状检测体的组合类

        :param shape: 一个形状检测体或形状检测体列表
        :param point: 坐标,它是一个包含x和y坐标的元组
        :param contrary: 一个布尔值，用于确定是否将结果取反。如果它被设置为True，返回值将取反，默认值到False(可选)
        """
        super().__init__(shape, point, contrary)
        self.collision_fun = collision_fun

    def add(self, mod, shape):
        self.is_this_class(shape)
        shape_ = self.copy()
        shape_.shape.append((mod, shape.collision_fun, shape.get_key()))
        return shape_

    def iadd(self, mod, shape):
        self.is_this_class(shape)
        self.shape.append((mod, shape.collision_fun, shape.get_key()))
        return self

    def get_key(self):
        return self.contrary, self.shape
