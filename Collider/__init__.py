from .polygon import Polygon
from .circle import Circle
from .rectangle import Rectangle


class Collider:

    def __init__(self, collider: list = None, opposite=False):
        if collider is None:
            self.collider = []
        else:
            self.collider = collider
        self.opposite = opposite

    def __to_unite(self):
        if not self.collider:
            self.collider.append('unite')
        if self.collider[0] != 'unite':
            self.collider = ['unite', self.collider]

    def __get_to_unite(self):
        if not self.collider:
            return ['unite']
        if self.collider[0] != 'unite':
            return ['unite', self.collider.copy()]
        return self.collider.copy()

    def __to_merge(self):
        if not self.collider:
            self.collider.append('merge')
        if self.collider[0] != 'merge':
            self.collider = ['merge', self.collider]

    def __get_to_merge(self):
        if not self.collider:
            return ['merge']
        if self.collider[0] != 'merge':
            return ['merge', self.collider.copy()]
        return self.collider.copy()

    def __iadd__(self, other):
        self.__to_unite()
        if isinstance(other, Collider):
            self.collider.append(other.collider)
        else:
            self.collider.append(other)
        return self

    def __isub__(self, other):
        self.__to_unite()
        other.opposite = not other.opposite
        self.collider.append(other)
        return self

    def __imul__(self, other):
        self.__to_merge()
        self.collider.append(other)
        return self
