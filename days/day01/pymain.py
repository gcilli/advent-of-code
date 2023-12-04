from utilities.pyutils import *


def solve_part_one():
    content = read_input(day=1)
    content = [keep_only_digits(line) for line in content]
    content = [int(f"{line[0]}{line[-1]}") for line in content]
    print(f"part 1: {sum(content)}")


def solve_part_two():
    content = read_input(day=1)

    # needed for fix :D
    fixes = {
        "oneight": "oneeight",
        "twone": "twoone",
        "threeight": "threeeight",
        "fiveight": "fiveeight",
        "sevenine": "sevennine",
        "eightwo": "eighttwo",
        "eighthree": "eightthree",
        "nineight": "nineeight"
    }

    spelled_out_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for i in range(len(content)):
        line = content[i]
        line = line.strip()
        for error, fix in fixes.items():
            line = line.replace(error, fix)
        for letters, digit in spelled_out_digits.items():
            line = line.replace(letters, digit)
        content[i] = line

    content = [keep_only_digits(line) for line in content]
    content = [int(f"{line[0]}{line[-1]}") for line in content]
    print(f"part 2: {sum(content)}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
