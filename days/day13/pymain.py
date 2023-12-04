import sys  # noqa
sys.path.append(
    "/home/gcilli/data/fun/advent_of_code/2023/advent-of-code")  # noqa

import re
from utilities.pyutils import *


def find_vertical_reflection(grid, fix=False):
    for i in range(len(grid[0])-1):
        width = min(i+1, len(grid[0])-i-1)
        left = [line[i-width+1: i+1] for line in grid]
        right = [line[i+1: i+width+1][::-1] for line in grid]

        if fix:
            flat_left, flat_right = "", ""
            for left_line, right_line in zip(left, right):
                flat_left += left_line.replace('#', '1').replace('.', '0')
                flat_right += right_line.replace('#', '1').replace('.', '0')

            if bin(int(flat_left, 2) ^ int(flat_right, 2)).count('1') == 1:
                return i + 1

        elif left == right:
            return i + 1

    return 0


def find_horizontal_reflection(grid, fix=False):
    for i in range(len(grid)-1):
        width = min(i+1, len(grid)-i-1)
        top = grid[i-width+1: i+1]
        bottom = grid[i+1: i+width+1][::-1]

        if fix:
            flat_top, flat_bot = "", ""
            for top_line, bot_line in zip(top, bottom):
                flat_top += top_line.replace('#', '1').replace('.', '0')
                flat_bot += bot_line.replace('#', '1').replace('.', '0')

            if bin(int(flat_top, 2) ^ int(flat_bot, 2)).count('1') == 1:
                return i + 1

        elif top == bottom:
            return i + 1

    return 0


def solve_part_one():
    content = read_input(day=13, delimiter='\n\n')

    ans = 0
    for grid in content:
        grid = grid.split('\n')
        ans += find_vertical_reflection(grid) + \
            100*find_horizontal_reflection(grid)

    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=13, delimiter='\n\n')

    ans = 0
    for grid in content:
        grid = grid.split('\n')
        ans += find_vertical_reflection(grid, fix=True) + \
            100*find_horizontal_reflection(grid, fix=True)

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
