from utilities.pyutils import *

import itertools
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


class Light:
    On = True
    off = False


def solve_part_one(content):
    timer = Timer()

    ans = 0
    for line in content.split("\n"):
        tokens = line.split(" ")
        indicators = [i == "#" for i in tokens[0][1:-1]]
        buttons = [tuple(map(int, i[1:-1].split(","))) for i in tokens[1:-1]]

        n_buttons = 1
        while n_buttons <= len(buttons):
            combs = itertools.combinations(buttons, n_buttons)

            found = False
            for comb in combs:
                button_pressed = [0] * len(indicators)
                for b in comb:
                    for light in b:
                        button_pressed[light] += 1
                button_pressed = [bp % 2 == 1 for bp in button_pressed]
                if button_pressed == indicators:
                    ans += len(comb)
                    found = True
                    break

            if found:
                break

            n_buttons += 1

    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    ans = 0
    for line in content.split("\n"):
        tokens = line.split(" ")
        buttons = [tuple(map(int, i[1:-1].split(","))) for i in tokens[1:-1]]
        joltage = tuple(map(int, tokens[-1][1:-1].split(",")))

        A = []
        b = []
        for i, j in enumerate(joltage):
            A.append([0] * len(buttons))
            b.append(j)
            for b_idx, button in enumerate(buttons):
                if i in button:
                    A[-1][b_idx] += 1

        A = np.array(A)
        b = np.array(b)

        # minimize the sum of all pressed buttons
        c = np.ones(len(buttons))

        # linear equations A @ x = b
        constraints = LinearConstraint(A, b, b)

        # all solutions >= 0
        bounds = Bounds(0, np.inf)

        # all solutions and variables are integers
        integrality = np.ones(len(buttons))

        result = milp(
            c=c, constraints=constraints, bounds=bounds, integrality=integrality
        )

        x_int = np.round(result.x).astype(int)
        ans += sum(x_int)

    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day10/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
