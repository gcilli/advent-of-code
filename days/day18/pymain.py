from utilities.pyutils import *


def solve(cmds):
    yoff = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
    xoff = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

    y, x = 0, 0
    points = [(y, x)]
    for dir, steps in cmds[:-1]:
        y += yoff[dir]*steps
        x += xoff[dir]*steps
        points.append((y, x))
    points.append((0, 0))

    # Pick's Theorem :D
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    area = 0
    outer = 0
    for p1, p2 in zip(points[:-1], points[1:]):
        y1, x1 = p1
        y2, x2 = p2
        area += 0.5*(x1*y2 - x2*y1)
        outer += + abs(y2-y1) + abs(x2 - x1)

    inner = area - outer/2 + 1
    return int(outer + inner)


def solve_part_one():
    content = read_input(day=18, delimiter='\n')

    cmds = []
    for line in content:
        dir, steps, _ = line.split()
        steps = int(steps)
        cmds.append((dir, steps))

    ans = solve(cmds)
    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=18, delimiter='\n')

    cmds = []
    for line in content:
        _, _, color = line.split()
        steps = int(color[2:7], 16)
        dir = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[color[7]]
        cmds.append((dir, steps))

    ans = solve(cmds)
    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
