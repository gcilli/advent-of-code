#include "utilities/cpputils.h"

#include <format>
#include <ranges>

#include <iostream>

inline std::int64_t parse_int(std::string_view sv)
{
    std::int64_t result = 0;
    for (char c : sv)
    {
        result = result * 10 + (c - '0');
    }
    return result;
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    std::int64_t ans{0};
    std::int64_t dial{50};

    for (const auto& line : utils::split(content, "\n"))
    {
        if (line.empty())
            continue;

        const char direction = line[0];
        const std::int64_t diff = parse_int(line.substr(1));

        if (direction == 'L')
        {
            dial = ((dial - diff) % 100 + 100) % 100;
        }
        else if (direction == 'R')
        {
            dial = (dial + diff) % 100;
        }

        ans += (dial == 0);
    }

    std::cout << std::format("Part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    std::int64_t ans{0};
    std::int64_t dial{50};

    for (const auto& line : utils::split(content, "\n"))
    {
        if (line.empty())
            continue;

        const char direction = line[0];
        const std::int64_t diff = parse_int(line.substr(1));

        if (direction == 'L')
        {
            const std::int64_t new_dial = dial - diff;
            ans += (new_dial < 0 ? (-new_dial - 1) / 100 + 1 : 0);
            ans -= (dial == 0);
            dial = ((new_dial % 100) + 100) % 100;
            ans += (dial == 0);
        }
        else if (direction == 'R')
        {
            ans += (dial + diff) / 100;
            dial = (dial + diff) % 100;
        }
    }
    std::cout << std::format("Part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    const std::string content = utils::read_file("2025/day01/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
