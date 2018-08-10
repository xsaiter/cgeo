import geo
from math import sqrt as m_sqrt


class Rectangle(object):
    __slots__ = ("v1", "v2")

    def __init__(self, v1, v2):
        """
        :param v1: bottom left point
        :param v2: top right point
        """
        self.v1 = v1
        self.v2 = v2

    @staticmethod
    def x1(r):
        return r.v1.x

    @staticmethod
    def x2(r):
        return r.v2.x

    @staticmethod
    def y1(r):
        return r.v1.y

    @staticmethod
    def y2(r):
        return r.v2.y


class Segment(object):
    __slots__ = ("p1", "p2")

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def distance2(self):
        return geo.Point.distance2(self.p1, self.p2)

    def distance(self):
        return m_sqrt(self.distance2())


class Range(object):
    __slots__ = ("l", "r")

    def __init__(self, l, r):
        self.l = l
        self.r = r


def intersect_ranges(s1, s2):
    if s1.l <= s2.l <= s1.r:
        return True, Range(s2.l, min(s1.r, s2.r))
    if s2.l <= s1.l <= s2.r:
        return True, Range(s1.l, min(s1.r, s2.r))
    return False, None


def get_area_of_intersection_rectangles(rects):
    n = len(rects)
    if n == 0:
        return 0

    if n == 1:
        return (rects[0].v1.x - rects[0].v2.x)*(rects[0].v1.y - rects[0].v2.y)

    def get_seg(fn1, fn2):
        res = Range(fn1(rects[0]), fn2(rects[0]))
        for i in range(1, n):
            cur = Range(fn1(rects[i]), fn2(rects[i]))
            t = intersect_ranges(res, cur)
            if t[0]:
                res = t[1]
            else:
                return False, None
        return True, res

    seg = get_seg(Rectangle.x1, Rectangle.x2)
    if not seg[0]:
        return 0
    x = seg[1]

    seg = get_seg(Rectangle.y1, Rectangle.y2)
    if not seg[0]:
        return 0
    y = seg[1]

    return (x.r - x.l)*(y.r - y.l)


class Polygon(object):
    def __init__(self, points):
        self.points = points

    def get_area(self):
        return get_area_of_polygon(self.points)


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

    return perimeter_one(Rectangle.y1, Rectangle.y2, Rectangle.x1, Rectangle.x2) + perimeter_one(Rectangle.x1, Rectangle.x2, Rectangle.y1, Rectangle.y2)


def segments_intersect(s1, s2):
    r1 = geo.cross_product(s1.p1, s1.p2, s2.p1)
    r2 = geo.cross_product(s1.p1, s1.p2, s2.p2)

    r3 = geo.cross_product(s2.p1, s2.p2, s1.p1)
    r4 = geo.cross_product(s2.p1, s2.p2, s1.p2)

    if ((r1 > 0 and r2 < 0) or (r1 < 0 and r2 > 0)) and ((r3 > 0 and r4 < 0) or (r3 < 0 and r4 > 0)):
        return True

    def is_point_on_segment(s, p):
        return max(s.p1.x, s.p2.x) >= p.x >= min(s.p1.x, s.p2.x) and max(s.p1.y, s.p2.y) >= p.y >= min(s.p1.y, s.p2.y)

    if r1 == 0:
        return is_point_on_segment(s1, s2.p1)

    if r2 == 0:
        return is_point_on_segment(s1, s2.p2)

    if r3 == 0:
        return is_point_on_segment(s2, s1.p1)

    if r4 == 0:
        return is_point_on_segment(s2, s1.p2)

    return False
