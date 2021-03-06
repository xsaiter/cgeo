import unittest
import geo
import shapes


def get_polygon():
    p1 = geo.Point(0, 0)
    p2 = geo.Point(5, 0)
    p3 = geo.Point(5, 2)
    p4 = geo.Point(2, 2)
    p5 = geo.Point(2, 6)
    p6 = geo.Point(0, 3)

    return [p1, p2, p3, p4, p5, p6]


class TestShapes(unittest.TestCase):
    def test_get_area_of_polygon(self):
        area = shapes.get_area_of_polygon(get_polygon())
        self.assertEqual(area, 15)

    def test_get_area_of_triangle(self):
        area = shapes.get_area_of_triangle(geo.Point(0, 0), geo.Point(5, 0), geo.Point(2, 10))
        self.assertEqual(area, 25)

    def test_get_total_perimeter_of_rectangles(self):
        r1 = shapes.Rectangle(geo.Point(1, 1), geo.Point(6, 4))
        r2 = shapes.Rectangle(geo.Point(5, 0), geo.Point(8, 2))
        r3 = shapes.Rectangle(geo.Point(7, 1), geo.Point(9, 4))
        r4 = shapes.Rectangle(geo.Point(4, 3), geo.Point(10, 6))

        actual = shapes.get_total_perimeter_of_rectangles([r1, r2, r3, r4])

        self.assertEqual(actual, 34)

    def test_segments_intersect(self):
        seg1 = shapes.Segment(geo.Point(1, 1), geo.Point(4, 4))
        seg2 = shapes.Segment(geo.Point(3, 2), geo.Point(5, 2))
        actual = shapes.segments_intersect(seg1, seg2)
        self.assertEquals(actual, False)

        seg2 = shapes.Segment(geo.Point(3, 2), geo.Point(1, 3))
        actual = shapes.segments_intersect(seg1, seg2)
        self.assertEquals(actual, True)

        seg2 = shapes.Segment(geo.Point(4, 4), geo.Point(5, 2))
        actual = shapes.segments_intersect(seg1, seg2)
        self.assertEquals(actual, True)

    def test_get_area_of_intersection_rectangles(self):
        r1 = shapes.Rectangle(geo.Point(0, 0), geo.Point(5, 3))
        r2 = shapes.Rectangle(geo.Point(3, 1), geo.Point(8, 4))

        actual = shapes.get_area_of_intersection_rectangles([r1, r2])
        self.assertEquals(actual, 4)


if __name__ == '__main__':
    unittest.main()
