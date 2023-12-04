#include <iostream>
#include <map>
#include <optional>

#include "utilities/cpputils.h"

std::optional<std::pair<std::pair<std::size_t, std::size_t>, char>> is_part_number(
    const std::vector<std::string>& content,
    const std::size_t i,
    const std::size_t j,
    const std::uint32_t num)
{
    using OutputType = std::pair<std::pair<std::size_t, std::size_t>, char>;

    const std::size_t num_digits{std::to_string(num).size()};
    if (content[i][j - num_digits - 1] != '.')
    {
        return OutputType{{i, j - num_digits - 1}, content[i][j - num_digits - 1]};
    }
    if (content[i][j] != '.')
    {
        return OutputType{{i, j}, content[i][j]};
    }
    for (std::size_t k{j - num_digits - 1}; k < j + 1; k++)
    {
        if (content[i - 1][k] != '.')
        {
            return OutputType{{i - 1, k}, content[i - 1][k]};
        }
        if (content[i + 1][k] != '.')
        {
            return OutputType{{i + 1, k}, content[i + 1][k]};
        }
    }
    return std::nullopt;
}

void solve_part_one()
{
    const std::vector<std::string> content = utils::pad_grid(utils::split(utils::read_input(3), "\n"), 1, '.');

    std::uint32_t ans{0U};
    std::uint32_t num{0U};

    for (std::size_t i{0U}; i < content.size(); i++)
    {
        for (std::size_t j{0U}; j < content[i].size(); j++)
        {
            const char& c = content[i][j];
            if (std::isdigit(c))
            {
                num = 10 * num + (c - '0');
            }
            else
            {
                ans += num * (num > 0 && is_part_number(content, i, j, num));
                num = 0;
            }
        }
    }

    std::cout << "part 1: " << ans << std::endl;
}

void solve_part_two()
{
    const std::vector<std::string> content = utils::pad_grid(utils::split(utils::read_input(3), "\n"), 1, '.');

    std::uint32_t ans{0U};
    std::uint32_t num{0U};
    std::map<std::pair<std::size_t, std::size_t>, std::vector<std::uint32_t>> symbols;

    for (std::size_t i{0U}; i < content.size(); i++)
    {
        for (std::size_t j{0U}; j < content[i].size(); j++)
        {
            const char& c = content[i][j];
            if (std::isdigit(c))
            {
                num = 10 * num + (c - '0');
            }
            else
            {
                if (num > 0)
                {
                    const auto part_number_opt = is_part_number(content, i, j, num);
                    if (part_number_opt)
                    {
                        const auto coords = part_number_opt.value().first;
                        const char symbol = part_number_opt.value().second;
                        if (symbol == '*')
                        {
                            symbols[coords].push_back(num);
                        }
                    }
                }
                num = 0;
            }
        }
    }

    // filter symbols to keep only those that are adjacent to two numbers
    for (const auto& [coords, nums] : symbols)
    {
        ans += (nums.size() == 2) * nums.front() * nums.back();
    }

    std::cout << "part 2: " << ans << std::endl;
}

int main()
{
    solve_part_one();
    solve_part_two();
}
