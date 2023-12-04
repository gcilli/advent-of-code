#include <iostream>
#include <regex>
#include <unordered_map>

#include "utilities/cpputils.h"

void solve_part_one()
{
    const std::vector<std::string> content{utils::split(utils::read_input(2), "\n")};

    std::unordered_map<std::string, int> availability = {
        {"red", 12},
        {"green", 13},
        {"blue", 14},
    };

    const std::regex regex("(\\d+) (\\w+)");

    std::uint32_t ans{0U};
    for (std::size_t i{0U}; i < content.size(); i++)
    {
        const std::string& line = content[i];

        bool game_is_possible{true};

        const std::string game_line = utils::split(line, ":")[1];
        const std::vector<std::string> sets = utils::split(game_line, ";");
        for (const auto& set : sets)
        {
            bool set_is_possible{true};

            std::sregex_iterator first_match(set.begin(), set.end(), regex);
            std::sregex_iterator last_match{};
            for (std::sregex_iterator iter = first_match; iter != last_match; iter++)
            {
                const std::smatch& match = *iter;
                const std::vector<std::string> cube = utils::split(match.str(), " ");

                const int amount = std::stoi(cube[0]);
                const std::string& color = cube[1];

                if (amount > availability[color])
                {
                    set_is_possible = false;
                    break;
                }
            }

            game_is_possible = !set_is_possible;
        }

        ans += (i + 1) * game_is_possible;
    }

    std::cout << "Part 1: " << ans << std::endl;
}

void solve_part_two()
{
    const std::vector<std::string> content{utils::split(utils::read_input(2), "\n")};

    std::regex regex("(\\d+) (\\w+)");

    std::uint32_t ans{0U};
    std::ranges::for_each(content, [&ans, &regex](const auto& line) -> void {
        std::unordered_map<std::string, int> requirements = {
            {"red", 0},
            {"green", 0},
            {"blue", 0},
        };

        const std::string game_line = utils::split(line, ":")[1];
        const std::vector<std::string> sets = utils::split(game_line, ";");
        for (const auto& set : sets)
        {
            std::sregex_iterator first_match(set.begin(), set.end(), regex);
            std::sregex_iterator last_match{};
            for (std::sregex_iterator iter = first_match; iter != last_match; iter++)
            {
                const std::smatch& match = *iter;
                const std::vector<std::string> cube = utils::split(match.str(), " ");

                const int amount = std::stoi(cube[0]);
                const std::string& color = cube[1];

                requirements[color] = std::max(requirements[color], amount);
            }
        }

        ans += requirements["red"] * requirements["green"] * requirements["blue"];
    });

    std::cout << "Part 2: " << ans << std::endl;
}

int main()
{
    solve_part_one();
    solve_part_two();
}
