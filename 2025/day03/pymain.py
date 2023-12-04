from utilities.pyutils import *


def parse_content(content):
    return [list(map(int, line)) for line in content.split("\n")]


def find_joltage(line, num_batteries):
    joltage = 0

    current_index = 0
    while len(str(joltage)) < num_batteries:
        slots = num_batteries - len(str(joltage)) if joltage != 0 else num_batteries
        best = max(line[current_index : len(line) - (slots - 1)])
        joltage = joltage * 10 + best
        current_index = line.index(best, current_index) + 1

    return joltage


def solve_part_one(content):
    timer = Timer()

    ans = 0
    for line in parse_content(content):
        ans += find_joltage(line, num_batteries=2)

    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    ans = 0
    for line in parse_content(content):
        ans += find_joltage(line, num_batteries=12)

    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day03/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
