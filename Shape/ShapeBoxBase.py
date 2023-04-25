try:
    from BaseShape import BaseShape
except ImportError:
    from .BaseShape import BaseShape


class ShapeBoxBase(BaseShape):

    def __init__(self, shape, point=(0, 0), centre=(0, 0), contrary=False):
        super().__init__(point, centre, contrary)
        if isinstance(shape, list):
            self.shape = shape
        elif issubclass(type(shape), BaseShape):
            self.shape = []
            self.__iadd_and(shape)

    def is_this_class(self, cls):
        if not isinstance(cls, self.__class__):
            raise TypeError(f"The type must be {self.__class__.__name__}")

    def iadd(self, mod, shape):
        pass

    def add(self, mod, shape):
        pass

    def __iadd_or(self, shape):
        return self.iadd('or', shape)

    def __iadd_and(self, shape):
        return self.iadd('and', shape)

    def __add_or(self, shape):
        return self.add('or', shape)

    def __add_and(self, shape):
        return self.add('and', shape)

    # region 重载运算符

    def __and__(self, other):
        return self.__add_and(other)

    def __or__(self, other):
        return self.__add_or(other)

    def __add__(self, other):
        return self.__add_or(other)

    def __iadd__(self, other):
        return self.__iadd_or(other)

    def __sub__(self, other):
        return self.__add_and(~other)

    def __isub__(self, other):
        return self.__iadd_and(~other)

    def __mul__(self, other):
        return self.__add_and(other)

    def __imul__(self, other):
        return self.__iadd_and(other)

    def __invert__(self):
        self.contrary = not self.contrary
        return self

    def __str__(self):
        return f"<{self.name}: point: {self.point}, contrary: {self.contrary}>"

    # endregion

    def copy(self):
        return ShapeBoxBase(self.shape, self.point, self.centre, self.contrary)
