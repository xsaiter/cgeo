import unittest
import geo
import convex_hull as ch


class TestConvexHull(unittest.TestCase):
    def test_graham_scan(self):
        points = generate_points()

        actual_hull = ch.graham_scan(points)
        expected_hull = get_expected_hull()

        self.assertEqual(actual_hull, expected_hull)

    def test_jarvis_march(self):
        points = generate_points()

        actual_hull = ch.jarvis_march(points)
        expected_hull = get_expected_hull()

        self.assertEqual(actual_hull, expected_hull)


def get_expected_hull():
    return [geo.Point(-2, -2), geo.Point(2, -2), geo.Point(7, 2), geo.Point(4, 6), geo.Point(-3, 2)]


def generate_points():
    p1 = geo.Point(-2, -2)
    p2 = geo.Point(2, -2)
    p3 = geo.Point(7, 2)
    p4 = geo.Point(4, 6)
    p5 = geo.Point(4, 4)
    p6 = geo.Point(2, 3)
    p7 = geo.Point(2, 1)
    p8 = geo.Point(1, 1)
    p9 = geo.Point(-1, 2)
    p10 = geo.Point(-3, 2)
    p11 = geo.Point(0, 0)

    return[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]


if __name__ == '__main__':
    unittest.main()
