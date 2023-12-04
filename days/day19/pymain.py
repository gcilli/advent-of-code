from utilities.pyutils import *
import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(50000)


def solve_part_one():
    content = read_input(day=19, delimiter='\n')
    ans = 0
    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input(day=19, delimiter='\n')
    ans = 0
    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
