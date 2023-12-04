from utilities.pyutils import *

import math


def solve_part_one():
    content = read_input(day=6)

    times = list(map(int, content[0].split(':')[1].split()))
    distances = list(map(int, content[1].split(':')[1].split()))

    ans = 1
    for t, d in zip(times, distances):
        s1 = 0.5 * (t - math.sqrt(t**2 - 4*d))
        s2 = 0.5 * (t + math.sqrt(t**2 - 4*d))

        # take values inside the range only.
        s1 = int(s1) + 1
        s2 = int(s2) - (s2 - int(s2) < 1e-4)

        ans *= s2 - s1 + 1

    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=6)

    t = int(''.join(content[0].split(':')[1].split()))
    d = int(''.join(content[1].split(':')[1].split()))

    s1 = 0.5 * (t - math.sqrt(t**2 - 4*d))
    s2 = 0.5 * (t + math.sqrt(t**2 - 4*d))

    # take values inside the range only.
    s1 = int(s1) + 1
    s2 = int(s2) - (s2 - int(s2) < 1e-4)

    ans = s2 - s1 + 1

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
