from utilities.pyutils import *

from collections import defaultdict


def solve_part_one():
    content = read_input(day=2)

    ans = 0
    availability = {"red": 12, "green": 13, "blue": 14}

    games = [[s.split(',') for s in line.split(':')[1].split(';')]
             for line in content]
    for index, game in enumerate(games, 1):
        for set in game:
            set_is_possible = True
            for cubes in set:
                amount, color = cubes.strip().split()
                if int(amount) > availability[color]:
                    set_is_possible = False

            if not set_is_possible:
                break
        else:
            ans += index

    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=2)

    ans = 0

    games = [[s.split(',') for s in line.split(':')[1].split(';')]
             for line in content]
    for game in games:
        reqs = defaultdict(int)
        for set in game:
            for cubes in set:
                amount, color = cubes.strip().split()
                reqs[color] = max(reqs[color], int(amount))

        ans += reqs["red"] * reqs["green"] * reqs["blue"]

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
