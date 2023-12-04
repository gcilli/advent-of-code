#include "utilities/cpputils.h"

#include <format>
#include <ranges>

#include <iostream>

void solve_part_one(auto lines)
{
    utils::Timer timer;

    std::int64_t ans{0};

    std::cout << std::format("Part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(auto lines)
{
    utils::Timer timer;

    std::int64_t ans{0};

    std::cout << std::format("Part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    std::string content = utils::read_file("2025/day10/inputs/input.txt");
    auto lines = utils::split(content, "\n");

    solve_part_one(lines);
    solve_part_two(lines);
}
