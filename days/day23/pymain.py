from utilities.pyutils import *
import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(50000)


def solve(grid, y, x, path, paths, no_slope=False):
    h, w = len(grid), len(grid[0])
    if (y, x) == (h-1, w-2):
        paths.append(path)
        return

    if not (0 <= y < h and 0 <= x < w):
        return

    if grid[y][x] == '#':
        return

    if grid[y][x] == '.' or no_slope:
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)][::-1]:
            if (y+dy, x+dx) not in path:
                solve(grid, y+dy, x+dx, path + [(y+dy, x+dx)], paths, no_slope)
    else:
        dy, dx = {'<': (0, -1), '>': (0, 1), 'v': (1, 0),
                  '^': (-1, 0)}[grid[y][x]]
        if (y+dy, x+dx) not in path:
            solve(grid, y+dy, x+dx, path + [(y+dy, x+dx)], paths, no_slope)

    return


def solve_part_one():
    grid = read_input_test(day=23, delimiter='\n')

    paths = []
    solve(grid, 0, 1, [(0, 1)], paths)
    paths.sort(key=lambda path: len(path), reverse=True)

    ans = len(paths[0])-1
    print(f"part 1: {ans}")


def solve_part_two():
    grid = read_input(day=23, delimiter='\n')

    paths = []
    solve(grid, 0, 1, [(0, 1)], paths, no_slope=True)
    paths.sort(key=lambda path: len(path), reverse=True)

    ans = len(paths[0])-1
    print(f"part 1: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()  # takes hours :D
