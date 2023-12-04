from utilities.pyutils import *


def point_is_in_polygon(polygon, point):
    px, py = point
    n = len(polygon)

    # check if point is a vertex
    if point in polygon:
        return True

    inside = False

    # ray-casting algorithm..
    # j points to the previous vertex. So, since the first vertex
    # we consider is at position 0, the previous one is at position n - 1
    j = n - 1

    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]

        # check if point is on horizontal edge
        if yi == yj == py and min(xi, xj) <= px <= max(xi, xj):
            return True

        # check if point is on vertical edge
        if xi == xj == px and min(yi, yj) <= py <= max(yi, yj):
            return True

        # only count vertical edges that cross our horizontal ray
        if xi == xj:
            if min(yi, yj) < py <= max(yi, yj) and xi > px:
                inside = not inside

        j = i

    return inside


def rectangle_inside_polygon_with_cache(
    polygon, rect_min_x, rect_max_x, rect_min_y, rect_max_y, cache, unique_x, unique_y
):
    # get the x coordinates to check (only those in unique_x that fall within rect bounds)
    x_coords_to_check = [x for x in unique_x if rect_min_x <= x <= rect_max_x]
    y_coords_to_check = [y for y in unique_y if rect_min_y <= y <= rect_max_y]

    if rect_min_x not in x_coords_to_check:
        x_coords_to_check.insert(0, rect_min_x)
    if rect_max_x not in x_coords_to_check:
        x_coords_to_check.append(rect_max_x)
    if rect_min_y not in y_coords_to_check:
        y_coords_to_check.insert(0, rect_min_y)
    if rect_max_y not in y_coords_to_check:
        y_coords_to_check.append(rect_max_y)

    # check the perimeters points (here the points are at discrete coordinates):

    # Top and bottom edges
    for x in x_coords_to_check:
        for y_edge in [rect_min_y, rect_max_y]:
            point = (x, y_edge)
            if point not in cache:
                cache[point] = point_is_in_polygon(polygon, point)
            if not cache[point]:
                return False

    # Left and right edges
    for y in y_coords_to_check:
        for x_edge in [rect_min_x, rect_max_x]:
            point = (x_edge, y)
            if point not in cache:
                cache[point] = point_is_in_polygon(polygon, point)
            if not cache[point]:
                return False

    return True


def solve_part_one(content):
    timer = Timer()

    red_tiles = []
    for line in content.split("\n"):
        if line.strip():
            x, y = map(int, line.split(","))
            red_tiles.append((x, y))

    max_area = 0

    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height

            max_area = max(max_area, area)

    ans = max_area
    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    polygon = []
    for line in content.split("\n"):
        if line.strip():
            x, y = map(int, line.split(","))
            polygon.append((x, y))

    # to close the polygon, first vertex is cloned at the end
    polygon.append(polygon[0])

    # pre-cache polygons bbox
    poly_min_x = min(p[0] for p in polygon)
    poly_max_x = max(p[0] for p in polygon)
    poly_min_y = min(p[1] for p in polygon)
    poly_max_y = max(p[1] for p in polygon)

    # extract unique x and y coordinates from the polygon
    unique_x = sorted(set(p[0] for p in polygon))
    unique_y = sorted(set(p[1] for p in polygon))

    # keep track of previously checked points
    point_cache = {}

    max_area = 0
    n = len(polygon) - 1

    for i in range(n):
        p1 = polygon[i]
        p1x, p1y = p1

        for j in range(i + 1, n):
            p2 = polygon[j]
            p2x, p2y = p2

            # get rect extremes
            if p1x <= p2x:
                min_x, max_x = p1x, p2x
            else:
                min_x, max_x = p2x, p1x

            if p1y <= p2y:
                min_y, max_y = p1y, p2y
            else:
                min_y, max_y = p2y, p1y

            height = max_y - min_y + 1
            width = max_x - min_x + 1
            area = height * width

            # check the area of the polygon.
            # if it's smaller than the biggest found so far, we can exclude it
            if area <= max_area:
                continue

            # check if rectangle is within polygon bbox. If not, skip it
            if (
                min_x < poly_min_x
                or max_x > poly_max_x
                or min_y < poly_min_y
                or max_y > poly_max_y
            ):
                continue

            if rectangle_inside_polygon_with_cache(
                polygon, min_x, max_x, min_y, max_y, point_cache, unique_x, unique_y
            ):
                max_area = area

    ans = max_area
    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day09/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
