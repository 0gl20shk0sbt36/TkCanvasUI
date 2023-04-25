try:
    from BaseShape import BaseShape
except ImportError:
    from .BaseShape import BaseShape


def collision_fun(shapes, point):
    req = True
    for mod, shape in shapes:
        req_ = shape.collision_fun(shape, point)
        if mod == 'or':
            req = req or req_
        elif mod == 'and':
            req = req and req_
    return req


class ShapeChangeableBox(BaseShape):

    def __init__(self, shape, point=(0, 0), centre=(0, 0), contrary=False):
        super().__init__(point, centre, contrary)
        self.collision_fun = collision_fun
        if isinstance(shape, list):
            self.shape = shape
        elif issubclass(type(shape), BaseShape):
            self.shape = []
            self.__iadd('and', shape)

    def __iadd(self, mod, shape: BaseShape):
        self.shape.append((mod, shape))

    def __add(self, mod, shape: BaseShape):
        shape_ = self.copy()
        shape_.__iadd(mod, shape)
        return shape_

    # region 重载运算符

    def __and__(self, other):
        return self.__add('and', other)

    def __or__(self, other):
        return self.__add('or', other)

    def __add__(self, other):
        return self.__add('or', other)

    def __iadd__(self, other):
        return self.__iadd('or', other)

    def __sub__(self, other):
        return self.__add('and', ~other)

    def __isub__(self, other):
        return self.__iadd('and', ~other)

    def __mul__(self, other):
        return self.__add('and', other)

    def __imul__(self, other):
        return self.__iadd('and', other)

    def __invert__(self):
        self.contrary = not self.contrary
        return self

    def __str__(self):
        return f"<{self.name}: point: {self.point}, contrary: {self.contrary}>"

    # endregion

    def copy(self):
        return ShapeChangeableBox(self.shape, self.point, self.centre, self.contrary)

    def collision(self, point):
        return self.collision_fun(self.shape, point)
