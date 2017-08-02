class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({self.x}, {self.y})".format(self=self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def cross_product(a, b, c):
    """
    > 0 if a, b, c - clockwise
    < 0 - counterclockwise
    = 0 - collinear
    """
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


def distance2(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    return dx * dx + dy * dy


def triangle_area_by_points(p1, p2, p3):
    return abs(cross_product(p1, p2, p3)) / 2


def polygon_area_by_points(points):
    res = 0
    n = len(points)

    if n < 2:
        return 0

    pivot = points[0]
    for i in range(1, n - 1):
        res += cross_product(pivot, points[i], points[i + 1]) / 2

    return abs(res)
