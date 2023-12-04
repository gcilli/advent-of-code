from utilities.pyutils import *


def parse_content(content):
    fresh_ranges, ids = content.split("\n\n")

    fresh_ranges = [tuple(map(int, f.split("-"))) for f in fresh_ranges.split("\n")]
    ids = list(map(int, ids.split("\n")))

    return fresh_ranges, ids


def solve_part_one(content):
    timer = Timer()

    fresh_ranges, ids = parse_content(content)

    ans = 0
    for id in ids:
        if any(fl <= id <= fr for fl, fr in fresh_ranges):
            ans += 1

    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    fresh_ranges, _ = parse_content(content)

    fresh_ranges.sort()

    # Merge overlapping ranges
    merged = [fresh_ranges[0]]
    for fl, fr in fresh_ranges[1:]:
        if fl <= merged[-1][1]:
            # Current range overlaps or is adjacent to the last merged range
            merged[-1] = (merged[-1][0], max(merged[-1][1], fr))
        else:
            merged.append((fl, fr))

    ans = sum(fr - fl + 1 for fl, fr in merged)

    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day05/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
