import math

from utilities.pyutils import *


def all_zeros(nums):
    for n in nums:
        if n != 0:
            return False
    return True


def solve_part_one():
    content = read_input(day=9)

    ans = 0
    for line in content:
        nums = list(map(int, line.split()))

        while not all_zeros(nums):
            ans += nums[-1]
            nums = [r-l for l, r in zip(nums[:-1], nums[1:])]

    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=9)

    ans = 0
    for line in content:
        nums = list(map(int, line.split()))

        first = []
        while not all_zeros(nums):
            first.append(nums[0])
            nums = [r-l for l, r in zip(nums[:-1], nums[1:])]
        for i in range(len(first)):
            ans += [-1, 1][i % 2 == 0] * first[i]

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
