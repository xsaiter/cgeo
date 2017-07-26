import functools
import geo


def graham_scan(points):
    hull = []
    n = len(points)
    if n <= 3:
        hull.extend(points)
        return hull

    first = leftmost_and_lowest(points)
    points[0], points[first] = points[first], points[0]

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


def jarvis_march(points):
    hull = []

    n = len(points)
    if n <= 3:
        hull.extend(points)
        return hull

    first = leftmost_and_lowest(points)
    visited = [first]
    hull.append(points[first])
    prev = first

    while True:
        cur = first
        for i in range(0, n):
            if i not in visited:
                r = geo.ccw(points[prev], points[i], points[cur])
                if r > 0:
                    cur = i
                elif r == 0:
                    d1 = geo.distance2(points[prev], points[i])
                    d2 = geo.distance2(points[prev], points[cur])
                    if d1 > d2:
                        cur = i

        if cur == first:
            break

        visited.append(cur)
        hull.append(points[cur])
        prev = cur

    return hull


def leftmost_and_lowest(points):
    def comp(a, b):
        if a.y > b.y:
            return 1

        if a.y == b.y:
            if a.x < b.x:
                return -1
            else:
                return 1

        return -1

    return points.index(min(points, key=functools.cmp_to_key(comp)))
