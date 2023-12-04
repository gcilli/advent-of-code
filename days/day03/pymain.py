from utilities.pyutils import *

from collections import defaultdict


def is_part_number(content, i, j, num):
    num_digits = len(str(num))
    if content[i][j-num_digits-1] != '.':
        return True, ((i, j-num_digits-1), content[i][j-num_digits-1])
    if content[i][j] != '.':
        return True, ((i, j), content[i][j])
    for k in range(j-num_digits-1, j+1):
        if content[i-1][k] != '.':
            return True, ((i-1, k), content[i-1][k])
        if content[i+1][k] != '.':
            return True, ((i+1, k), content[i+1][k])
    return False, (None, None)


def solve_part_one():
    content = pad(read_input(day=3), 1, '.')

    ans, num = 0, 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            c = content[i][j]
            if c in get_digits_as_string():
                num = 10*num + int(c)
            else:
                if num > 0 and is_part_number(content, i, j, num)[0]:
                    ans += num
                num = 0

    print(f"part 1: {ans}")


def solve_part_two():
    content = pad(read_input(day=3), 1, '.')

    ans, num, symbols = 0, 0, defaultdict(list)
    for i in range(len(content)):
        for j in range(len(content[i])):
            c = content[i][j]
            if c in get_digits_as_string():
                num = 10*num + int(c)
            else:
                if num > 0:
                    result, (coords, symbol) = is_part_number(
                        content, i, j, num)
                    if result:
                        if symbol == '*':
                            symbols[coords].append(num)
                num = 0

    # filter symbols to keep only those that are adjacent to two numbers
    for nums in symbols.values():
        if len(nums) == 2:
            ans += nums[0] * nums[1]

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
