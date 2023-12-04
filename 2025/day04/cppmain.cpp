#include "utilities/cpputils.h"

#include <ranges>

#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_set>
#include <vector>

std::vector<std::string> parse_content(const std::string& content)
{
    std::vector<std::string> grid;
    for (auto row : utils::split(content, "\n"))
    {
        grid.emplace_back(row);
    }
    return grid;
}

std::pair<bool, std::uint64_t> find_n_accessible_rolls(auto& grid, bool update_grid = false)
{
    std::uint64_t n_accessible{0};

    // precompute the offsets
    auto offsets = std::views::cartesian_product(std::views::iota(-1, 2), std::views::iota(-1, 2)) |
                   std::views::filter([](auto pair) { return !(pair.first == 0 && pair.second == 0); });

    // precompute height and width
    const std::size_t height{grid.size()};
    if (height == 0)
    {
        return {};
    }
    const std::size_t width{grid[0].size()};

    bool grid_changed{false};
    for (auto [y, row] : std::views::enumerate(grid))
    {
        for (auto [x, cell] : std::views::enumerate(row))
        {
            if (cell == '.')
            {
                continue;
            }

            std::size_t neighbors_count{0U};
            for (auto [dy, dx] : offsets)
            {
                const std::size_t ny = y + dy;
                const std::size_t nx = x + dx;

                if (ny < height && nx < width && grid[ny][nx] == '@')
                {
                    neighbors_count++;
                    if (neighbors_count >= 4)
                    {
                        // it is not needed to get exactly the number of neighbors..
                        // the fact that they are more than 4 is sufficient.
                        break;
                    }
                }
            }

            if (neighbors_count < 4)
            {
                n_accessible++;

                // needed for part two
                if (update_grid)
                {
                    grid[y][x] = '.';
                    grid_changed = true;
                }
            }
        }
    }

    return {grid_changed, n_accessible};
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    std::vector<std::string> grid = parse_content(content);

    auto [_, n_accessible] = find_n_accessible_rolls(grid, false);

    std::uint64_t ans{n_accessible};

    std::cout << std::format("Part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    std::vector<std::string> grid = parse_content(content);

    std::uint64_t ans{0U};
    while (true)
    {
        auto [grid_changed, n_accessible] = find_n_accessible_rolls(grid, true);
        if (!grid_changed)
        {
            break;
        }
        ans += n_accessible;
    }

    std::cout << std::format("Part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    const std::string content = utils::read_file("2025/day04/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
