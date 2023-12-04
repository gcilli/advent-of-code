from utilities.pyutils import *


def solve(content, width_of_empty_space):
    empty_rows = [i for i in range(len(content)) if '#' not in content[i]]
    empty_cols = [j for j in range(len(content[0])) if '#' not in [
        content[i][j] for i in range(len(content))]]

    galaxies = [(i, j) for i in range(len(content))
                for j in range(len(content[i])) if content[i][j] == '#']

    ans = 0
    for y1, x1 in galaxies:
        for y2, x2 in galaxies:
            if (y1, x1) == (y2, x2):
                continue

            steps = 0
            for row in range(y1+1, y2+1):
                steps += width_of_empty_space if row in empty_rows else 1
            for col in range(x1+1, x2+1):
                steps += width_of_empty_space if col in empty_cols else 1

            ans += steps

    return ans


def solve_part_one():
    content = read_input(day=11)
    ans = solve(content, width_of_empty_space=2)
    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=11)
    ans = solve(content, width_of_empty_space=1_000_000)
    print(f"part 1: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
