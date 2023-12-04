from utilities.pyutils import *


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i, j


def solve_part_one():
    grid = pad(read_input(day=21, delimiter='\n'), width=1, char='#')

    y, x = find_start(grid)

    positions = set()
    positions.add((y, x))
    steps = 64
    for _ in range(steps):
        new_positions = set()
        for y, x in positions:
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if grid[y+dy][x+dx] != '#':
                    new_positions.add((y+dy, x+dx))

        positions = new_positions

    ans = len(positions)
    print(f"part 1: {ans}")


def solve_part_two():
    ans = 0
    print(f"part 1: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()  # takes hours :D
