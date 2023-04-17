from os import chdir
from os.path import split
from TkCanvasUI2.Collider import *


def main():
    c = Collider()
    # p = Polygon((0, 0), (100, 0), (100, 100), (0, 100), point=(10, 10))
    # c += p
    print(c.get_to_merge())
    # p = Polygon((0, 0), (100, 0), (100, 100), (0, 100), point=(10, 10))
    # c *= p
    print(c.get_to_merge())


if __name__ == '__main__':
    chdir(split(__file__)[0])
    main()
