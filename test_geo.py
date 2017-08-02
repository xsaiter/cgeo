import unittest
import geo


def get_polygon():
    p1 = geo.Point(0, 0)
    p2 = geo.Point(5, 0)
    p3 = geo.Point(5, 2)
    p4 = geo.Point(2, 2)
    p5 = geo.Point(2, 6)
    p6 = geo.Point(0, 3)

    return [p1, p2, p3, p4, p5, p6]


class TestGeo(unittest.TestCase):
    def test_polygon_area_by_points(self):
        area = geo.polygon_area_by_points(get_polygon())
        self.assertEqual(area, 15)

    def test_triangle_area_by_points(self):
        area = geo.triangle_area_by_points(geo.Point(0, 0), geo.Point(5, 0), geo.Point(2, 10))
        self.assertEqual(area, 25)


if __name__ == '__main__':
    unittest.main()
