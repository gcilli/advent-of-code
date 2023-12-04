#include "utilities/cpputils.h"

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

struct Region
{
    std::uint16_t width;
    std::uint16_t height;
    std::vector<std::uint16_t> quantities;
};

std::vector<Region> parse_regions(const std::string& regions_section)
{
    std::vector<Region> regions;
    std::stringstream ss(regions_section);
    std::string line;

    while (std::getline(ss, line))
    {
        if (line.empty())
            continue;

        auto colon_pos = line.find(':');
        if (colon_pos == std::string::npos)
            continue;

        const std::string dimensions = line.substr(0, colon_pos);
        const std::string quantities_str = line.substr(colon_pos + 1);

        const std::size_t x_pos = dimensions.find('x');
        if (x_pos == std::string::npos)
            continue;

        const std::uint16_t width = std::stoi(dimensions.substr(0, x_pos));
        const std::uint16_t height = std::stoi(dimensions.substr(x_pos + 1));

        std::vector<std::uint16_t> quantities;
        std::stringstream qs(quantities_str);
        std::uint16_t q{};
        while (qs >> q)
        {
            quantities.push_back(q);
        }

        regions.push_back({width, height, quantities});
    }

    return regions;
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    std::vector<std::string> sections;
    std::stringstream ss(content);
    std::string accumulator;
    std::string line;

    while (std::getline(ss, line))
    {
        if (line.empty())
        {
            if (!accumulator.empty())
            {
                sections.push_back(accumulator);
                accumulator.clear();
            }
        }
        else
        {
            if (!accumulator.empty())
            {
                accumulator += "\n";
            }
            accumulator += line;
        }
    }
    if (!accumulator.empty())
    {
        sections.push_back(accumulator);
    }

    const std::uint8_t num_shapes = sections.size() - 1;
    const std::uint8_t shape_area = 9;

    // parse regions (last section)
    const std::vector<Region> regions = parse_regions(sections[sections.size() - 1]);

    std::uint64_t ans = 0;
    for (const auto& region : regions)
    {
        std::uint64_t region_area = region.width * region.height;

        std::uint64_t shapes_area_total = 0;
        for (std::size_t i = 0; i < region.quantities.size() && i < num_shapes; ++i)
        {
            shapes_area_total += shape_area * region.quantities[i];
        }

        if (shapes_area_total <= region_area)
        {
            ans += 1;
        }
    }

    std::cout << "part 1 (runtime: " << timer.elapsed_ms() << "ms): " << ans << "\n";
}

int main()
{
    const std::string content = utils::read_file("2025/day12/inputs/input.txt");

    solve_part_one(content);
}
