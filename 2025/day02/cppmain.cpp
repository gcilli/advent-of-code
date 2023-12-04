#include "utilities/cpputils.h"

#include <format>
#include <ranges>

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// Cache for generated sequences
std::unordered_map<std::uint16_t, std::unordered_set<std::uint64_t>> cache_part_one;
std::unordered_map<std::uint16_t, std::unordered_set<std::uint64_t>> cache_part_two;

// Integer power function to avoid floating-point operations
constexpr std::uint64_t int_pow(std::uint64_t base, unsigned int exp)
{
    std::uint64_t result = 1;
    for (unsigned int i = 0; i < exp; ++i)
    {
        result *= base;
    }
    return result;
}

std::unordered_set<std::uint64_t> generate_all_possible_sequences(const std::uint64_t min_value,
                                                                  const std::uint64_t max_value,
                                                                  const std::uint8_t repeated_count)
{
    std::unordered_set<std::uint64_t> result;
    result.reserve(max_value - min_value);

    for (std::uint64_t seq = min_value; seq < max_value; ++seq)
    {
        std::uint64_t repeated_seq = 0;
        std::uint64_t temp = seq;

        // Calculate the number by repeating digits
        for (std::uint8_t i = 0; i < repeated_count; ++i)
        {
            std::uint64_t multiplier = 1;
            std::uint64_t temp_copy = temp;
            while (temp_copy > 0)
            {
                multiplier *= 10;
                temp_copy /= 10;
            }
            repeated_seq = repeated_seq * multiplier + temp;
        }

        result.insert(repeated_seq);
    }

    return result;
}

std::unordered_set<std::uint64_t> get_invalid_ids_with_n_digits_part_one(const unsigned int n_digits)
{
    // Check cache first
    if (cache_part_one.find(n_digits) != cache_part_one.end())
    {
        return cache_part_one[n_digits];
    }

    // If n_digits is odd, we cannot have a sequence repeated exactly twice
    if (n_digits % 2 != 0)
    {
        return {};
    }

    const unsigned int half_len = n_digits / 2;
    const std::uint64_t min_value = int_pow(10, half_len - 1);
    const std::uint64_t max_value = int_pow(10, half_len);
    auto result = generate_all_possible_sequences(min_value, max_value, 2);

    cache_part_one[n_digits] = result;
    return result;
}

std::unordered_set<std::uint64_t> get_invalid_ids_with_n_digits_part_two(const unsigned int n_digits)
{
    // Check cache first
    if (cache_part_two.find(n_digits) != cache_part_two.end())
    {
        return cache_part_two[n_digits];
    }

    auto divisors = std::views::iota(1U, n_digits / 2U + 1U) |
                    std::views::filter([n_digits](auto div) { return n_digits % div == 0; });

    std::unordered_set<std::uint64_t> invalid_ids = {};

    for (std::uint8_t div : divisors)
    {
        const std::uint8_t repeat_count = n_digits / div;
        if (repeat_count < 2)
        {
            continue;
        }

        const std::uint8_t half_len = div;
        const std::uint64_t min_value = int_pow(10, half_len - 1);
        const std::uint64_t max_value = int_pow(10, half_len);
        invalid_ids.merge(generate_all_possible_sequences(min_value, max_value, repeat_count));
    }

    cache_part_two[n_digits] = invalid_ids;
    return invalid_ids;
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    std::uint64_t ans{0U};
    auto ranges = utils::split(content, ",");

    for (const auto& range : ranges)
    {
        std::string range_str(range);
        auto tokens = utils::split(range_str, "-");

        auto it = std::ranges::begin(tokens);
        const std::uint64_t first = std::stoull(std::string(*it++));
        const std::uint64_t last = std::stoull(std::string(*it));

        const std::uint8_t first_n_digits = std::to_string(first).length();
        const std::uint8_t last_n_digits = std::to_string(last).length();

        for (std::uint8_t n = first_n_digits; n < last_n_digits + 1; n++)
        {
            for (const std::uint64_t invalid_id : get_invalid_ids_with_n_digits_part_one(n))
            {
                if (first <= invalid_id && invalid_id <= last)
                {
                    ans += invalid_id;
                }
            }
        }
    }

    std::cout << std::format("Part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    std::uint64_t ans{0U};
    auto ranges = utils::split(content, ",");

    for (const auto& range : ranges)
    {
        std::string range_str(range);
        auto tokens = utils::split(range_str, "-");

        auto it = std::ranges::begin(tokens);
        const std::uint64_t first = std::stoull(std::string(*it++));
        const std::uint64_t last = std::stoull(std::string(*it));

        const std::uint8_t first_n_digits = std::to_string(first).length();
        const std::uint8_t last_n_digits = std::to_string(last).length();

        for (std::uint8_t n = first_n_digits; n < last_n_digits + 1; n++)
        {
            for (const std::uint64_t id : get_invalid_ids_with_n_digits_part_two(n))
            {
                if (first <= id && id <= last)
                {
                    ans += id;
                }
            }
        }
    }

    std::cout << std::format("Part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    const std::string content = utils::read_file("2025/day02/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
