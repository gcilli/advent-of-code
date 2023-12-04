from utilities.pyutils import *


def generate_all_possible_sequences(min_value, max_value, repeated_count):
    result = set()
    for seq in range(min_value, max_value):
        # Repeat the sequence repeated_count times to get n_digits
        repeated_seq = int(str(seq) * repeated_count)
        result.add(repeated_seq)
    return result


def get_invalid_ids_with_n_digits_part_one(n_digits):
    # If n_digits is odd, we cannot have a sequence repeated exactly twice
    if n_digits % 2 != 0:
        return []

    half_len = n_digits // 2
    min_value = 10 ** (half_len - 1)
    max_value = 10**half_len
    return generate_all_possible_sequences(min_value, max_value, 2)


def get_invalid_ids_with_n_digits_part_two(n_digits):
    invalid_ids = set()

    for div in range(1, n_digits // 2 + 1):
        if n_digits % div != 0:
            continue

        repeat_count = n_digits // div
        if repeat_count < 2:
            continue

        half_len = div
        min_value = 10 ** (half_len - 1)
        max_value = 10**half_len
        invalid_ids.update(
            generate_all_possible_sequences(min_value, max_value, repeat_count)
        )

    return invalid_ids


def solve_part_one(content):
    timer = Timer()

    ans = 0
    for r in content.split(","):
        first, last = map(int, r.split("-"))

        first_n_digits = len(str(first))
        last_n_digits = len(str(last))

        for n in range(first_n_digits, last_n_digits + 1):
            for invalid_id in get_invalid_ids_with_n_digits_part_one(n):
                if first <= invalid_id <= last:
                    ans += invalid_id

    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    ans = 0
    for r in content.split(","):
        first, last = map(int, r.split("-"))

        first_n_digits = len(str(first))
        last_n_digits = len(str(last))

        for n in range(first_n_digits, last_n_digits + 1):
            for invalid_id in get_invalid_ids_with_n_digits_part_two(n):
                if first <= invalid_id <= last:
                    ans += invalid_id

    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day02/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
