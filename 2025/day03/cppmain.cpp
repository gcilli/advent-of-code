#include "utilities/cpputils.h"

#include <format>
#include <ranges>

#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_set>
#include <vector>

std::uint64_t find_voltage(const auto line, const std::uint8_t num_batteries)
{
    std::vector<int> joltage;

    std::size_t current_index = 0;
    while (joltage.size() < num_batteries)
    {
        std::size_t slots = num_batteries - joltage.size();
        std::size_t window_size = std::ranges::distance(line) - slots + 1;

        auto window = line | std::views::drop(current_index) | std::views::take(window_size - current_index);
        auto best_it = std::ranges::max_element(window);

        joltage.push_back(*best_it);
        current_index += std::ranges::distance(window.begin(), best_it) + 1;
    }

    return std::accumulate(joltage.begin(), joltage.end(), 0ULL, [](std::uint64_t l, int r) { return l * 10 + r; });
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    std::uint64_t ans{0U};
    for (const auto& range : utils::split(content, "\n"))
    {
        auto line = range | std::views::transform([](char c) { return c - '0'; });
        ans += find_voltage(line, 2);
    }

    std::cout << std::format("Part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    std::uint64_t ans{0U};
    for (const auto& range : utils::split(content, "\n"))
    {
        auto line = range | std::views::transform([](char c) { return c - '0'; });
        ans += find_voltage(line, 12);
    }

    std::cout << std::format("Part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    const std::string content = utils::read_file("2025/day03/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
