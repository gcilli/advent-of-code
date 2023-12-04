from utilities.pyutils import *


def tilt_north(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            c = grid[i][j]
            if c == 'O':
                k = i-1
                while k >= 0 and grid[k][j] == '.':
                    k -= 1
                    continue
                grid[i][j] = '.'
                grid[k+1][j] = 'O'
    return grid


def tilt_south(grid):
    for i in range(len(grid)-1, -1, -1):
        for j in range(len(grid[i])):
            c = grid[i][j]
            if c == 'O':
                k = i+1
                while k < len(grid) and grid[k][j] == '.':
                    k += 1
                    continue
                grid[i][j] = '.'
                grid[k-1][j] = 'O'
    return grid


def tilt_west(grid):
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            c = grid[i][j]
            if c == 'O':
                k = j-1
                while k >= 0 and grid[i][k] == '.':
                    k -= 1
                    continue
                grid[i][j] = '.'
                grid[i][k+1] = 'O'
    return grid


def tilt_east(grid):
    for j in range(len(grid[0])-1, -1, -1):
        for i in range(len(grid)):
            c = grid[i][j]
            if c == 'O':
                k = j+1
                while k < len(grid[i]) and grid[i][k] == '.':
                    k += 1
                    continue
                grid[i][j] = '.'
                grid[i][k-1] = 'O'
    return grid


def count_load(grid):
    load = 0
    for i, line in enumerate(grid[::-1], 1):
        load += i*len([c for c in line if c == 'O'])
    return load


def find_loop(loads):
    if len(loads) == 1:
        return None
    for i, load in enumerate(loads[:-1]):
        if load == loads[-1]:
            return (i, len(loads)-1)

    return None


def solve_part_one():
    grid = read_input(day=14)

    for i in range(len(grid)):
        grid[i] = [c for c in grid[i]]

    tilted_grid = tilt_north(grid)

    ans = count_load(tilted_grid)
    print(f"part 1: {ans}")


def solve_part_two():
    grid = read_input(day=14)

    for i in range(len(grid)):
        grid[i] = [c for c in grid[i]]

    loads = []

    num_cycles = 1_000_000_000
    cycle = 0
    while cycle < num_cycles:
        loop = find_loop(loads)
        if loop is not None:
            length = loop[1] - loop[0]
            cycle += length * ((num_cycles - cycle) // length)

        grid = tilt_north(grid)
        load_north = count_load(grid)

        grid = tilt_west(grid)
        load_west = count_load(grid)

        grid = tilt_south(grid)
        load_south = count_load(grid)

        grid = tilt_east(grid)
        load_east = count_load(grid)

        loads.append(f"n{load_north}-w{load_west}-s{load_south}-e{load_east}")

        cycle += 1

    ans = count_load(grid)
    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
