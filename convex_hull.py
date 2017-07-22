import functools
import geo


def graham_scan(points):
    hull = []
    n = len(points)
    if n <= 3:
        hull.extend(points)
        return hull

    min_y_pos = 0
    min_y = points[0].y

    for i in range(1, n):
        if points[i].y < min_y:
            min_y = points[i].y
            min_y_pos = i

    points[0], points[min_y_pos] = points[min_y_pos], points[0]

    pivot = points[0]

    def angle_cmp(x, y):
        r = geo.ccw(pivot, x, y)
        if r > 0:
            return 1
        if r < 0:
            return -1
        return 1 if geo.distance2(pivot, x) > geo.distance2(pivot, y) else -1

    points = points[:1] + sorted(points[1:], key=functools.cmp_to_key(angle_cmp), reverse=True)

    hull.extend(points[:3])

    for i in range(3, n):
        while True:
            top = hull.pop()
            next_top = hull.pop()

            hull.append(next_top)
            hull.append(top)

            if geo.ccw(next_top, top, points[i]) == -1:
                hull.pop()
            else:
                hull.append(points[i])
                break

    return hull
