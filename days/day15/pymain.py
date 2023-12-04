from utilities.pyutils import *


def hash(seq):
    value = 0
    for c in seq:
        value += ord(c)
        value *= 17
        value %= 256
    return value


def parse_seq(seq):
    if '=' in seq:
        return seq[:seq.index("=")], hash(seq[:seq.index('=')]), '=', int(seq[-1])
    return seq[:seq.index('-')], hash(seq[:seq.index('-')]), '-', None


def solve_part_one():
    content = read_input(day=15, delimiter=',')

    ans = 0
    for seq in content:
        ans += hash(seq)

    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=15, delimiter=',')

    labels, focals = [[] for _ in range(256)], [[] for _ in range(256)]
    for seq in content:
        label, box, op, focal = parse_seq(seq)

        if op == '-':
            if label in labels[box]:
                index = labels[box].index(label)
                labels[box].remove(label)
                focals[box].pop(index)
        else:
            if label in labels[box]:
                index = labels[box].index(label)
                focals[box][index] = focal
            else:
                labels[box].append(label)
                focals[box].append(focal)

    ans = 0
    for box_number, focal in enumerate(focals, 1):
        for lens_id, f in enumerate(focal, 1):
            ans += box_number * lens_id * f

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
