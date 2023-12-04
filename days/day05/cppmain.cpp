#include <array>
#include <iostream>
#include <ranges>
#include <vector>

#include "utilities/cpputils.h"

std::pair<std::vector<std::uint64_t>, std::vector<std::vector<std::array<std::uint64_t, 3U>>>> parse_input()
{
    const std::vector<std::string> content = utils::split(utils::read_input(5), "\n\n");
    const std::vector<std::uint64_t> seeds = utils::get_vector_of_numbers(utils::split(content[0], ":")[1], " ");

    std::vector<std::vector<std::array<std::uint64_t, 3U>>> mappings;
    for (std::size_t i{1U}; i < content.size(); i++)
    {
        const auto lines = utils::split(content[i], "\n");
        std::vector<std::array<std::uint64_t, 3U>> mapping;
        for (std::size_t j{1U}; j < lines.size(); j++)
        {
            const auto data = utils::get_vector_of_numbers(lines[j], " ");
            mapping.push_back({data[1U], data[0U], data[2U]});
        }
        mappings.push_back(mapping);
    }

    return std::make_pair(seeds, mappings);
}

void solve_part_one()
{
    auto [seeds, mappings] = parse_input();

    std::uint64_t ans{1000000000000000000U};
    for (auto& seed : seeds)
    {
        for (const auto& mapping : mappings)
        {
            for (const auto& [source, dest, length] : mapping)
            {
                if (source <= seed && seed < source + length)
                {
                    seed = dest + (seed - source);
                    break;
                }
            }
        }
        ans = std::min(ans, seed);
    }

    std::cout << "part 1: " << ans << std::endl;
}

void solve_part_two()
{
    const auto [seeds, mappings] = parse_input();

    std::vector<std::pair<std::uint64_t, std::uint64_t>> new_seeds;
    for (std::size_t i{0U}; i < seeds.size(); i += 2)
    {
        new_seeds.push_back(std::make_pair(seeds[i], seeds[i + 1]));
    }

    std::uint64_t ans{0U};
    while (true)
    {
        std::uint64_t seed{ans};
        for (const auto& mapping : mappings | std::views::reverse)
        {
            for (const auto& [source, dest, length] : mapping)
            {
                if (dest <= seed && seed < dest + length)
                {
                    seed = source + (seed - dest);
                    break;
                }
            }
        }

        for (const auto& [s1, l] : new_seeds)
        {
            if (s1 <= seed && seed <= s1 + l)
            {
                std::cout << "part 2: " << ans << std::endl;
                return;
            }
        }

        ans++;
    }
}

int main()
{
    solve_part_one();
    solve_part_two();
}
