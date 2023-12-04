from utilities.pyutils import *


def solve_part_one(content):
    timer = Timer()

    ans = 0
    dial = 50
    for line in content.split("\n"):
        diff = int(line[1:])
        if line[0] == "L":
            dial = (dial - diff) % 100
        else:
            dial = (dial + diff) % 100

        ans += dial == 0

    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    ans = 0
    dial = 50
    for line in content.split("\n"):
        d = int(line[1:])
        if line[0] == "L":
            ans += abs((dial - d) // 100) - (dial == 0)
            dial = (dial - d) % 100
            ans += dial == 0
        else:
            ans += (dial + d) // 100
            dial = (dial + d) % 100

    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day01/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
