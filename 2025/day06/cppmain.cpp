#include "utilities/cpputils.h"

#include <charconv>
#include <ranges>

#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_set>
#include <vector>

void solve_part_one(const std::string& content)
{
    const utils::Timer timer;

    auto lines_ranges = utils::split(content, "\n");
    const auto lines_count = std::ranges::distance(lines_ranges);

    // parse numbers
    std::vector<std::vector<std::uint16_t>> numbers;
    numbers.reserve(lines_count - 1);

    auto numbers_lines = lines_ranges | std::views::take(lines_count - 1);
    for (auto number_line : numbers_lines)
    {
        std::vector<std::uint16_t> line;
        line.reserve(2048U);

        // take all numbers removing whitespaces between them
        for (auto number_range : number_line | std::views::split(' ') |
                                     std::views::filter([](auto&& rng) { return std::ranges::distance(rng) > 0; }))
        {
            std::uint16_t number{};
            std::from_chars(number_range.begin(), number_range.end(), number);
            line.push_back(std::move(number));
        }

        numbers.push_back(std::move(line));
    }

    // parse operations
    std::vector<char> ops;
    ops.reserve(2048U);

    auto ops_line = lines_ranges | std::views::drop(lines_count - 1);
    for (auto op_range : std::string(*ops_line.begin()) | std::views::split(' ') |
                             std::views::filter([](auto&& rng) { return std::ranges::distance(rng) > 0; }))
    {
        char op = *op_range.begin();
        ops.push_back(std::move(op));
    }

    std::uint64_t ans{0};

    for (std::size_t i = 0; i < ops.size(); ++i)
    {
        // Extract column i from all rows
        auto column = numbers | std::views::transform([i](const auto& row) { return row[i]; });

        ans += (ops[i] == '+') ? std::reduce(column.begin(), column.end(), 0ULL)
                               : std::reduce(column.begin(), column.end(), 1ULL, std::multiplies<>{});
    }

    std::cout << std::format("Part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    auto lines_ranges = utils::split(content, "\n");
    const auto lines_count = std::ranges::distance(lines_ranges);

    std::vector<std::vector<char>> lines;
    lines.reserve(lines_count - 1);

    auto content_lines = lines_ranges | std::views::take(lines_count - 1);
    for (auto line_view : content_lines)
    {
        // this time, no split is done as we want to keep the alignment
        std::vector<char> line(line_view.begin(), line_view.end());
        lines.push_back(line);
    }

    std::string ops_str;
    auto ops_line = lines_ranges | std::views::drop(lines_count - 1);
    for (auto op_view : ops_line)
    {
        ops_str = std::string(op_view);
    }

    // add dots to fill in the gaps and keep the alignment
    const std::size_t num_cols = lines[0].size();
    const std::size_t num_rows = lines.size();

    for (std::size_t i = 0; i < num_cols; ++i)
    {
        bool has_non_space = false;

        // check whether we are in between a section of two consecutive groups of numbers (in column)
        for (std::size_t j = 0; j < num_rows; ++j)
        {
            if (lines[j][i] != ' ')
            {
                has_non_space = true;
                break;
            }
        }

        // current number has smaller width that the other numbers on the same column. Let's add a dot to keep the
        // alignment
        if (has_non_space)
        {
            for (std::size_t j = 0; j < num_rows; ++j)
            {
                if (lines[j][i] == ' ')
                {
                    lines[j][i] = '.';
                }
            }
        }
    }

    // now that we are sure that all numbers are aligned (via dots), we can split each line by spaces
    std::vector<std::vector<std::string>> lines_of_numbers;
    for (const auto& line : lines)
    {
        std::vector<std::string> numbers;
        std::string number;
        for (char c : line)
        {
            if (c == ' ')
            {
                numbers.push_back(number);
                number.clear();
            }
            else
            {
                number += c;
            }
        }

        numbers.push_back(number);
        lines_of_numbers.push_back(numbers);
    }

    // Split ops by spaces
    auto ops_view = ops_str | std::views::filter([](char c) { return c != ' '; });
    std::vector<char> ops(ops_view.begin(), ops_view.end());

    std::uint64_t ans{0};
    for (std::size_t i = 0; i < ops.size(); ++i)
    {
        char op = ops[i];

        // get all digits at position i from each part
        auto digits = lines_of_numbers | std::views::transform([i](const auto& line) { return line[i]; });

        std::vector<std::uint64_t> nums;
        for (std::size_t j = 0; j < digits.front().size(); ++j)
        {
            // build number string column-wise, removing dots
            auto num_str = digits | std::views::transform([j](const auto& digit) { return digit[j]; }) |
                           std::views::filter([](char c) { return c != '.'; });

            std::string cleaned(num_str.begin(), num_str.end());
            if (!cleaned.empty())
            {
                nums.push_back(std::stoull(cleaned));
            }
        }

        // perform operations
        ans += (op == '+') ? std::reduce(nums.begin(), nums.end(), 0ULL)
                           : std::reduce(nums.begin(), nums.end(), 1ULL, std::multiplies<>{});
    }

    std::cout << std::format("Part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    const std::string content = utils::read_file("2025/day06/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
