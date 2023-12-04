from utilities.pyutils import *


def parse_content(content):
    content = content.split("\n\n")

    shapes_section = content[:-1]
    regions_section = content[-1]

    shapes = [block.split(":")[1].strip().split("\n") for block in shapes_section]
    regions = [
        (
            int(line.split(":")[0].split("x")[0]),
            int(line.split(":")[0].split("x")[1]),
            tuple(map(int, line.split(":")[1].strip().split(" "))),
        )
        for line in regions_section.split("\n")
    ]

    return shapes, regions


def solve_part_one(content):
    timer = Timer()

    shapes, regions = parse_content(content)

    ans = 0
    for w, h, quantities in regions:
        area = w * h

        shapes_area_total = 0
        for i, q in enumerate(quantities):
            shape = shapes[i]

            shape_area = sum(row.count("#") for row in shape)
            shapes_area_total += shape_area * q

        if shapes_area_total > area:
            continue

        ans += 1

    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day12/inputs/input.txt")

    solve_part_one(content)
