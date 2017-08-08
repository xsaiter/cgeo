import geo


def get_area_of_triangle(p1, p2, p3):
    return abs(geo.cross_product(p1, p2, p3)) / 2


def get_area_of_polygon(points):
    res = 0
    n = len(points)

    if n < 2:
        return 0

    pivot = points[0]
    for i in range(1, n - 1):
        res += geo.cross_product(pivot, points[i], points[i + 1]) / 2

    return abs(res)


class Rectangle(object):
    __slots__ = ("v1", "v2")

    def __init__(self, v1, v2):
        """
        :param v1: bottom left point
        :param v2: top right point
        """
        self.v1 = v1
        self.v2 = v2


def get_segments_count(items):
    items = sorted(items, key=lambda i: i[0], reverse=False)

    s = 0
    res = 0

    for item in items:
        s += item[1]
        if s == 0:
            res += 1

    return res


def get_total_perimeter_of_rectangles(rectangles):
    def perimeter_one(a1, a2, b1, b2):
        res = 0

        sections = sorted(set([a1(r) for r in rectangles] + [a2(r) for r in rectangles]))
        for i in range(0, len(sections) - 1):
            mn = sections[i]
            mx = sections[i + 1]

            in_rectangles = list(filter(lambda r: a1(r) < mx and a2(r) > mn, rectangles))

            items = []
            for rect in in_rectangles:
                items.append((b1(rect), -1))
                items.append((b2(rect), 1))

            n = get_segments_count(items)

            res += n * (mx - mn) * 2

        return res

    def x1(r):
        return r.v1.x

    def x2(r):
        return r.v2.x

    def y1(r):
        return r.v1.y

    def y2(r):
        return r.v2.y

    return perimeter_one(y1, y2, x1, x2) + perimeter_one(x1, x2, y1, y2)
