#include "utilities/cpputils.h"

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct PairHash
{
    std::size_t operator()(const std::pair<int, int>& p) const
    {
        return std::hash<int>()(p.first) ^ (std::hash<int>()(p.second) << 1);
    }
};

auto parse_content(const std::string& content)
{
    std::vector<std::string> grid;
    std::stringstream ss(content);
    std::string line;
    while (std::getline(ss, line))
    {
        grid.push_back(line);
    }

    // find start position
    int start_y = -1, start_x = -1;
    for (int y = 0; y < static_cast<int>(grid.size()); y += 2)
    {
        for (int x = 0; x < static_cast<int>(grid[y].size()); ++x)
        {
            if (grid[y][x] == 'S')
            {
                start_y = y;
                start_x = x;
                break;
            }
        }
        if (start_y != -1)
            break;
    }

    return std::make_pair(grid, std::make_pair(start_y, start_x));
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    auto [grid, start] = parse_content(content);

    std::uint64_t ans = 0;
    std::unordered_set<std::pair<int, int>, PairHash> beams;
    beams.insert({start.first, start.second});

    for (int step = start.first; step < static_cast<int>(grid.size()) - 1; ++step)
    {
        std::unordered_set<std::pair<int, int>, PairHash> new_beams;

        for (const auto& [beam_y, beam_x] : beams)
        {
            if (grid[beam_y + 1][beam_x] == '^')
            {
                new_beams.insert({beam_y + 1, beam_x - 1});
                new_beams.insert({beam_y + 1, beam_x + 1});
                ans++;
            }
            else
            {
                new_beams.insert({beam_y + 1, beam_x});
            }
        }

        beams = new_beams;
    }

    std::cout << std::format("Part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    auto [grid, start] = parse_content(content);

    std::unordered_set<std::pair<int, int>, PairHash> beams;
    beams.insert({start.first, start.second});

    std::unordered_map<std::pair<int, int>, uint64_t, PairHash> timelines;
    timelines[{start.first, start.second}] = 1;

    for (int step = start.first; step < static_cast<int>(grid.size()) - 1; ++step)
    {
        std::unordered_set<std::pair<int, int>, PairHash> new_beams;
        std::unordered_map<std::pair<int, int>, uint64_t, PairHash> new_timelines;

        for (const auto& [beam_y, beam_x] : beams)
        {
            uint64_t current_timelines = timelines[{beam_y, beam_x}];

            if (grid[beam_y + 1][beam_x] == '^')
            {
                auto beam_left = std::make_pair(beam_y + 1, beam_x - 1);
                auto beam_right = std::make_pair(beam_y + 1, beam_x + 1);

                new_beams.insert(beam_left);
                new_timelines[beam_left] += current_timelines;

                new_beams.insert(beam_right);
                new_timelines[beam_right] += current_timelines;
            }
            else
            {
                auto next_beam = std::make_pair(beam_y + 1, beam_x);
                new_beams.insert(next_beam);
                new_timelines[next_beam] += current_timelines;
            }
        }

        beams = new_beams;
        timelines = new_timelines;
    }

    uint64_t ans = 0;
    int last_row = static_cast<int>(grid.size()) - 1;
    for (const auto& [pos, count] : timelines)
    {
        if (pos.first == last_row)
        {
            ans += count;
        }
    }

    std::cout << std::format("Part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    const std::string content = utils::read_file("2025/day07/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
