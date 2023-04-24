class Circle:

    def __init__(self, radius, point, opposite=False):
        """ 圆类

        :param point: 圆心坐标
        :param radius: 半径
        """
        self.point = point
        self.radius = radius ** 2
        self.opposite = opposite

    def __str__(self):
        return f"Circle(point={self.point}, radius={self.radius})"

    def collider(self, point):
        """ 判断点是否在圆内

        :param point: 点的坐标
        :return: 点是否在圆内
        """
        return (((self.point[0] - point[0]) ** 2 + (self.point[1] - point[1]) ** 2) < self.radius) ^ self.opposite
