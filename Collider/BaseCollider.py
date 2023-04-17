class BaseCollider:

    def __init__(self, point=(0, 0), opposite=False):
        self.point = point
        self.opposite = opposite
    
    def collision(self, point):
