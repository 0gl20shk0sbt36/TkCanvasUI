try:
    from ShapeBoxBase import ShapeBoxBase
except ImportError:
    from .ShapeBoxBase import ShapeBoxBase


def collision_fun(cls, point):
    req = True
    for mod, shape in cls.shape:
        req_ = shape.collision_fun(shape, point)
        if mod == 'or':
            req = req or req_
        elif mod == 'and':
            req = req and req_
    return req ^ cls.contrary


class ShapeChangeableBox(ShapeBoxBase):

    def __init__(self, shape, point=(0, 0), contrary=False):
        super().__init__(shape, point, contrary)
        self.collision_fun = collision_fun

    def iadd(self, mod, shape):
        self.shape.append((mod, shape))

    def add(self, mod, shape):
        shape_ = self.copy()
        shape_.iadd(mod, shape)
        return shape_

    def get_mbr(self):
        pass

    def get_key(self):
        return self
