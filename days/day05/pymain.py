from utilities.pyutils import *


def parse_inputs():
    content = read_input(5, delimiter='\n\n')
    seeds = list(map(int, content[0].split(':')[1].split()))

    mappings = []
    for lines in content[1:]:
        lines = lines.split('\n')[1:]
        mapping = []
        for line in lines:
            dest, source, length = list(map(int, line.split()))
            mapping.append((source, dest, length))
        mappings.append(mapping)

    return seeds, mappings


def solve_part_one():
    seeds, mappings = parse_inputs()

    ans = 1e100
    for seed in seeds:
        for mapping in mappings:
            for source, dest, length in mapping:
                if source <= seed < source + length:
                    seed = dest + (seed - source)
                    break
        ans = min(ans, seed)

    print(f"part 1: {ans}")


def solve_part_two():
    seeds, mappings = parse_inputs()
    seeds = [(s1, l) for s1, l in zip(seeds[::2], seeds[1::2])]

    ans = 0
    while True:
        seed = ans
        for mapping in mappings[::-1]:
            for source, dest, length in mapping:
                if dest <= seed < dest + length:
                    seed = source + (seed - dest)
                    break

        for s1, l in seeds:
            if s1 <= seed <= s1+l:
                print(f"part 2: {ans}")
                return

        ans += 1


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
