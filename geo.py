class Point(object):
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({self.x}, {self.y})".format(self=self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def distance2(a, b):
        dx = a.x - b.x
        dy = a.y - b.y
        return dx * dx + dy * dy


def cross_product(a, b, c):
    """
    > 0 if a, b, c - clockwise
    < 0 - counterclockwise
    = 0 - collinear
    """
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

