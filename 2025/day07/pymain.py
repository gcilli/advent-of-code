from utilities.pyutils import *

from collections import defaultdict


def parse_content(content):
    grid = [list(row) for row in content.split("\n")]
    for y in range(0, len(grid), 2):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = (y, x)

    return grid, start


def solve_part_one(content):
    timer = Timer()

    grid, start = parse_content(content)

    splits = 0
    beams = [start]
    for _ in range(start[0], len(grid) - 1):
        new_beams = set()
        for beam_y, beam_x in beams:
            if grid[beam_y + 1][beam_x] == "^":
                new_beams.add((beam_y + 1, beam_x - 1))
                new_beams.add((beam_y + 1, beam_x + 1))
                splits += 1
            else:
                new_beams.add((beam_y + 1, beam_x))

        beams = new_beams

    ans = splits
    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    grid, start = parse_content(content)

    beams = [start]
    timelines = {start: 1}
    for _ in range(start[0], len(grid) - 1):
        new_beams = set()
        new_timelines = defaultdict(int)

        for beam_y, beam_x in beams:
            if grid[beam_y + 1][beam_x] == "^":
                beam_left = (beam_y + 1, beam_x - 1)
                beam_right = (beam_y + 1, beam_x + 1)

                # add timelines for left beam
                new_beams.add(beam_left)
                new_timelines[beam_left] += timelines[(beam_y, beam_x)]

                # add timelines for right beam
                new_beams.add(beam_right)
                new_timelines[beam_right] += timelines[(beam_y, beam_x)]

            else:
                next_beam = (beam_y + 1, beam_x)
                new_beams.add(next_beam)
                new_timelines[next_beam] += timelines[(beam_y, beam_x)]

        beams = new_beams
        timelines = new_timelines

    ans = 0
    for k, v in timelines.items():
        if k[0] == len(grid) - 1:
            ans += v

    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day07/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
