from utilities.pyutils import *


def is_connected(s1, s2, dir):
    if s2 == '.':
        return False
    if s1 == '|':
        return (dir == (-1, 0) and s2 in ['S', '|', 'F', '7']) or \
               (dir == (1, 0) and s2 in ['S', '|', 'L', 'J'])
    if s1 == '-':
        return (dir == (0, 1) and s2 in ['S', '-', '7', 'J']) or \
               (dir == (0, -1) and s2 in ['S', '-', 'F', 'L'])
    if s1 == 'L':
        return (dir == (0, 1) and s2 in ['S', '-', 'J', '7']) or \
               (dir == (-1, 0) and s2 in ['S', '|', 'F', '7'])
    if s1 == 'J':
        return (dir == (0, -1) and s2 in ['S', '-', 'L', 'F']) or \
               (dir == (-1, 0) and s2 in ['S', '|', 'F', '7'])
    if s1 == 'F':
        return (dir == (0, 1) and s2 in ['S', '-', 'J', '7']) or \
               (dir == (1, 0) and s2 in ['S', '|', 'L', 'J'])
    if s1 == '7':
        return (dir == (0, -1) and s2 in ['S', '-', 'L', 'F']) or \
               (dir == (1, 0) and s2 in ['S', '|', 'L', 'J'])
    if s1 == 'S':
        return (dir == (-1, 0) and s2 in ['|', 'F', '7']) or \
               (dir == (0, 1) and s2 in ['-', '7', 'J']) or \
               (dir == (1, 0) and s2 in ['|', 'L', 'J']) or \
               (dir == (0, -1) and s2 in ['-', 'F', 'L'])


def get_starting_pos(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == 'S':
                return y, x


def get_path(grid):
    ys, xs = get_starting_pos(grid)

    path, y1, x1, not_allowed_dir = [], ys, xs, None
    while True:
        path.append((y1, x1))
        s1 = grid[y1][x1]
        for dir_y, dir_x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if (dir_y, dir_x) == not_allowed_dir:
                continue
            s2 = grid[y1 + dir_y][x1 + dir_x]
            if is_connected(s1, s2, (dir_y, dir_x)):
                y1, x1 = y1 + dir_y, x1 + dir_x
                not_allowed_dir = (-dir_y, -dir_x)
                break
        if (y1, x1) == (ys, xs):
            break

    return path


def solve_part_one():
    grid = pad(read_input(day=10), 1, '.')
    path = get_path(grid)
    ans = len(path)//2
    print(f"part 1: {ans}")


def solve_part_two():
    grid = pad(read_input(day=10), 1, '.')
    path = get_path(grid)
    path.append(path[0])

    area = 0
    outer = 0
    for p1, p2 in zip(path[:-1], path[1:]):
        y1, x1 = p1
        y2, x2 = p2
        area += 0.5*(x1*y2 - x2*y1)
        outer += + abs(y2-y1) + abs(x2 - x1)

    ans = int(abs(area) - outer/2 + 1)
    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
