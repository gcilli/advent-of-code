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

auto parse_content(const std::string& content)
{
    auto parts = utils::split(content, "\n\n");
    auto parts_it = parts.begin();
    std::string fresh_ranges_part(*parts_it++);
    std::string ids_part(*parts_it);

    std::vector<std::pair<std::uint64_t, std::uint64_t>> fresh_ranges;
    fresh_ranges.reserve(100);

    for (const auto& line_view : utils::split(fresh_ranges_part, "\n"))
    {
        if (line_view.empty())
            continue;

        const auto dash_pos = line_view.find('-');

        if (dash_pos == std::string_view::npos)
            continue;

        std::uint64_t first{0U};
        std::uint64_t last{0U};
        std::from_chars(line_view.data(), line_view.data() + dash_pos, first);
        std::from_chars(line_view.data() + dash_pos + 1, line_view.data() + line_view.size(), last);

        fresh_ranges.emplace_back(first, last);
    }

    std::vector<std::uint64_t> ids;
    for (const auto& line_view : utils::split(ids_part, "\n"))
    {
        if (line_view.empty())
            continue;
        std::string id_str(line_view);
        ids.push_back(std::stoull(id_str));
    }

    return std::make_pair(fresh_ranges, ids);
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    const auto [fresh_ranges, ids] = parse_content(content);

    // Parse and check IDs
    std::uint64_t ans{0U};
    for (const std::uint64_t& id : ids)
    {
        for (const auto& [first, last] : fresh_ranges)
        {
            if (first <= id && id <= last)
            {
                ans += 1;
                break;
            }
        }
    }

    std::cout << std::format("Part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    auto [fresh_ranges, ids] = parse_content(content);

    // Sort ranges by start position
    std::sort(fresh_ranges.begin(), fresh_ranges.end());

    // Merge overlapping ranges
    std::vector<std::pair<std::uint64_t, std::uint64_t>> merged;
    merged.reserve(fresh_ranges.size());

    for (const auto& [fl, fr] : fresh_ranges)
    {
        if (!merged.empty() && fl <= merged.back().second + 1)
        {
            // Overlapping or adjacent - extend the last range
            merged.back().second = std::max(merged.back().second, fr);
        }
        else
        {
            merged.emplace_back(fl, fr);
        }
    }

    auto range_sizes = merged | std::views::transform([](const auto& range) { return range.second - range.first + 1; });

    std::uint64_t ans = std::accumulate(std::ranges::begin(range_sizes), std::ranges::end(range_sizes), 0ULL);

    std::cout << std::format("Part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    const std::string content = utils::read_file("2025/day05/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
