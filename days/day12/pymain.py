import sys  # noqa
sys.path.append(
    "/home/gcilli/data/fun/advent_of_code/2023/advent-of-code")  # noqa

import re
from utilities.pyutils import *


def get_arrangement(seq):
    return list(map(len, re.findall(r"(#+)", ''.join(seq))))


def solve(seq, ci, gt_arr, ans, step):
    while ci < len(seq) and seq[ci] != '?':
        ci += 1

    if '?' not in seq:
        if get_arrangement(seq) == gt_arr:
            print(f"{' '*step}SOLUTION: ", ''.join(seq), ans)
            ans += 1
        else:
            print(f"{' '*step}NOT A SOLUTION: ", ''.join(seq), ans)
        return ans

    for c in ['.', '#']:
        seq[ci] = c
        print(f"{' '*step}{''.join(seq)} hello")
        arr = get_arrangement(seq[:ci+1])

        if len(arr) > len(gt_arr):
            print(f"{' '*step}{''.join(seq)}, {arr}, {gt_arr}",
                  "not going deeper 1")
            continue

        min_num_arrs = min(len(arr), len(gt_arr))
        for i in range(min_num_arrs-1):
            if arr[i] != gt_arr[i]:
                print(f"{' '*step}{''.join(seq)}, {arr}, {gt_arr}",
                      "not going deeper 2")
                break
        else:
            if len(arr) == 0:
                print(f"{' '*step}{''.join(seq)}, {arr}, {gt_arr}")
                ans = solve([c for c in seq], ci+1, gt_arr, ans, step+1)

            elif arr[min_num_arrs-1] <= gt_arr[min_num_arrs-1]:
                diff = gt_arr[min_num_arrs-1] - arr[min_num_arrs-1]
                print(
                    f"{' '*step}{''.join(seq)}, {arr}, {gt_arr} - need to extend by {diff} --> seq: ", end='')

                for j in range(1, min(len(seq)-ci, diff+1)):
                    if seq[ci+j] in ['#', '?']:
                        seq[ci+j] = '#'
                    else:
                        print(f"{' '*step}{''.join(seq)}",
                              "not going deeper 3")
                        break
                else:
                    print(f"{' '*step}{''.join(seq)}")
                    # input()
                    ans = solve([c for c in seq], ci+1, gt_arr, ans, step+1)

            else:
                print(f"{' '*step}{''.join(seq)}, {arr}, {gt_arr}",
                      "not going deeper 4")

    return ans


def solve_part_one():
    content = read_input_test(day=12)

    ans = 0
    for i, line in enumerate(content):
        # print(f"{i/len(content)*100:.2f}", end='\r')
        print()
        seq, gt_arr = line.split()
        print(seq)
        gt_arr = list(map(int, gt_arr.split(',')))
        ans += solve([c for c in seq], 0, gt_arr, 0, 0)

    print(f"part 1: {ans}")


def solve_part_two():
    content = read_input_test(day=12)

    ans = 0
    for i, line in enumerate(content):
        # print(f"{i/len(content)*100:.2f}", end='\r')
        seq, gt_arr = line.split()
        seq = '?'.join([seq for _ in range(1)])

        gt_arr = ','.join([gt_arr for _ in range(1)])
        gt_arr = list(map(int, gt_arr.split(',')))

        nums = solve([c for c in seq], 0, gt_arr, 0)
        ans += nums
        print(seq, nums)
        # input()

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    # solve_part_two()
