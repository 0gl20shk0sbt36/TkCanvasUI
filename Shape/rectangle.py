class Rectangle:

    def __init__(self, width, height, point):
        self.point = point
        self.width = width
        self.height = height

    def collision(self, x, y):
        return self.point[0] <= x <= self.point[0] + self.width and self.point[1] <= y <= self.point[1] + self.height
