from utilities.pyutils import *


def parse_content(content):
    grid = content.split("\n")
    grid = pad(grid, width=1, char=".")
    grid = [list(row) for row in grid]
    return grid


def find_n_accessible_rolls(grid, update_grid=False):
    n_accessible = 0

    offsets = [
        (dy, dx) for dy in range(-1, 2) for dx in range(-1, 2) if (dy, dx) != (0, 0)
    ]

    grid_changed = False
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == ".":
                continue

            neighbors_count = 0
            for dy, dx in offsets:
                if grid[row + dy][col + dx] == "@":
                    neighbors_count += 1
                if neighbors_count >= 4:
                    break

            if neighbors_count < 4:
                n_accessible += 1

                # needed for part two
                if update_grid:
                    grid[row][col] = "."
                    grid_changed = True

    return grid, grid_changed, n_accessible


def solve_part_one(content):
    timer = Timer()

    grid = parse_content(content)

    _, _, n_accessible = find_n_accessible_rolls(grid)

    ans = n_accessible

    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    grid = parse_content(content)

    ans = 0

    grid_changed = True
    while grid_changed:
        grid, grid_changed, n_accessible = find_n_accessible_rolls(
            grid, update_grid=True
        )

        ans += n_accessible

    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day04/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
