from utilities.pyutils import *
import re


def parse_content(content, strip=True):
    content = content.split("\n")

    if strip:
        lines = [list(map(int, content[i].split())) for i in range(len(content) - 1)]
        ops = content[-1].split()
    else:
        lines = [[s for s in content[i]] for i in range(len(content) - 1)]
        ops = content[-1]

    return lines, ops


def solve_part_one(content):
    timer = Timer()

    lines, ops = parse_content(content)

    ans = 0
    for i, op in enumerate(ops):
        nums = [line[i] for line in lines]
        if op == "+":
            ans += sum(nums)
        else:
            acc = 1
            for n in nums:
                acc *= n
            ans += acc

    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    lines, ops = parse_content(content, strip=False)

    for i, op in enumerate(ops):
        if any([line[i] != " " for line in lines]):
            for j in range(len(lines)):
                # fill the gap with '.' so that later on it is easier to parse numbers
                lines[j][i] = "." if lines[j][i] == " " else lines[j][i]

    for j in range(len(lines)):
        lines[j] = "".join(lines[j]).split()
    ops = ops.split()

    ans = 0
    for i in range(len(ops)):
        op = ops[i]
        digits = [p[i] for p in lines]

        nums = []
        for j in range(len(digits[0])):
            n = "".join([d[j] for d in digits])
            nums.append(int(n.replace(".", "")))

        if op == "+":
            acc = sum(nums)
        elif op == "*":
            acc = 1
            for n in nums:
                acc *= n

        ans += acc

    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day06/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
