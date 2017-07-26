class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({self.x}, {self.y})".format(self=self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def ccw(a, b, c):
    p = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    if p < 0:
        return -1
    if p > 0:
        return 1
    return 0


def distance2(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    return dx * dx + dy * dy
