from utilities.pyutils import *
import sys
sys.setrecursionlimit(10000)


class Direction:
    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)


def in_grid(position, grid):
    y, x = position
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def shoot(grid, position, direction, energized_tiles, visited):
    if (position, direction) in visited:
        return

    y1, x1 = position
    dy, dx = direction
    energized_tiles[y1][x1] = 1
    visited.add((position, direction))

    if grid[y1][x1] == '.':
        y2, x2 = (y1 + dy, x1 + dx)
        if in_grid((y2, x2), grid):
            shoot(grid, (y2, x2), direction, energized_tiles, visited)

    if grid[y1][x1] == '\\':
        y2, x2 = (y1 + dx, x1 + dy)
        if in_grid((y2, x2), grid):
            shoot(grid, (y2, x2), (dx, dy), energized_tiles, visited)

    if grid[y1][x1] == '/':
        y2, x2 = (y1 - dx, x1 - dy)
        if in_grid((y2, x2), grid):
            shoot(grid, (y2, x2), (-dx, -dy), energized_tiles, visited)

    if grid[y1][x1] == '-':
        if dy == 0:
            y2, x2 = (y1 + dy, x1 + dx)
            if in_grid((y2, x2), grid):
                shoot(grid, (y2, x2), direction, energized_tiles, visited)
        else:
            y2_1, x2_1 = (y1 + dx, x1 + dy)
            if in_grid((y2_1, x2_1), grid):
                shoot(grid, (y2_1, x2_1), (dx, dy), energized_tiles, visited)

            y2_2, x2_2 = (y1 - dx, x1 - dy)
            if in_grid((y2_2, x2_2), grid):
                shoot(grid, (y2_2, x2_2), (-dx, -dy), energized_tiles, visited)

    if grid[y1][x1] == '|':
        if dy != 0:
            y2, x2 = (y1 + dy, x1 + dx)
            if in_grid((y2, x2), grid):
                shoot(grid, (y2, x2), direction, energized_tiles, visited)
        else:
            y2_1, x2_1 = (y1 + dx, x1 + dy)
            if in_grid((y2_1, x2_1), grid):
                shoot(grid, (y2_1, x2_1), (dx, dy), energized_tiles, visited)

            y2_2, x2_2 = (y1 - dx, x1 - dy)
            if in_grid((y2_2, x2_2), grid):
                shoot(grid, (y2_2, x2_2), (-dx, -dy), energized_tiles, visited)


def solve_part_one():
    grid = read_input(day=16, delimiter='\n')

    energized_tiles = [[0 for t in line] for line in grid]

    position = (0, 0)
    direction = Direction.right
    shoot(grid, position, direction, energized_tiles, set())

    ans = sum([sum(tiles) for tiles in energized_tiles])
    print(f"part 1: {ans}")


def solve_part_two():
    grid = read_input(day=16, delimiter='\n')

    ans = 0
    for i in range(len(grid)):
        position = (i, 0)
        direction = Direction.right
        energized_tiles = [[0 for t in line] for line in grid]
        shoot(grid, position, direction, energized_tiles, set())
        ans = max(ans, sum([sum(tiles) for tiles in energized_tiles]))

        position = (i, len(grid[i])-1)
        direction = Direction.left
        energized_tiles = [[0 for t in line] for line in grid]
        shoot(grid, position, direction, energized_tiles, set())
        ans = max(ans, sum([sum(tiles) for tiles in energized_tiles]))

    for j in range(len(grid[0])):
        position = (0, j)
        direction = Direction.down
        energized_tiles = [[0 for t in line] for line in grid]
        shoot(grid, position, direction, energized_tiles, set())
        ans = max(ans, sum([sum(tiles) for tiles in energized_tiles]))

        position = (len(grid)-1, j)
        direction = Direction.up
        energized_tiles = [[0 for t in line] for line in grid]
        shoot(grid, position, direction, energized_tiles, set())
        ans = max(ans, sum([sum(tiles) for tiles in energized_tiles]))

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
