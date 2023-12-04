#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string_view>
#include <unordered_map>

#include "utilities/cpputils.h"

std::vector<int> extract_digits(const std::string& s)
{
    const std::string digits{"0123456789"};
    std::vector<int> out{};
    for (const char c : s)
    {
        if (digits.find(c) != std::string::npos)
        {
            out.push_back(c - '0');
        }
    }
    return out;
}

void solve_part_one()
{
    const std::vector<std::string> content = utils::split(utils::read_input(1), "\n");

    std::uint32_t ans{0U};
    std::ranges::for_each(content, [&ans](const std::string& line) -> void {
        std::vector<int> digits;
        std::ranges::for_each(line, [&digits](const char c) {
            if (std::isdigit(c))
            {
                digits.push_back(c - '0');
            }
        });
        ans += 10 * digits.front() + digits.back();
    });
    std::cout << "Part 1: " << ans << std::endl;
}

void solve_part_two()
{
    std::vector<std::string> content = utils::split(utils::read_input(1), "\n");

    const std::unordered_map<std::string, std::string> fixes{
        {"oneight", "oneeight"},
        {"twone", "twoone"},
        {"threeight", "threeeight"},
        {"fiveight", "fiveeight"},
        {"sevenine", "sevennine"},
        {"eightwo", "eighttwo"},
        {"eighthree", "eightthree"},
        {"nineight", "nineeight"},
    };

    const std::unordered_map<std::string, std::string> spelled_out_digits{
        {"one", "1"},
        {"two", "2"},
        {"three", "3"},
        {"four", "4"},
        {"five", "5"},
        {"six", "6"},
        {"seven", "7"},
        {"eight", "8"},
        {"nine", "9"},
    };

    std::uint32_t ans{0U};
    std::ranges::for_each(content, [&ans, &fixes, &spelled_out_digits](std::string& line) -> void {
        std::ranges::for_each(fixes, [&line](const auto& item) {
            const auto& [error, fix] = item;
            std::size_t it{0U};
            while ((it = line.find(error)) != std::string::npos)
            {
                line.replace(it, error.size(), fix);
            }
        });

        std::ranges::for_each(spelled_out_digits, [&line](const auto& item) {
            const auto& [letters, digit] = item;
            std::size_t it{0U};
            while ((it = line.find(letters)) != std::string::npos)
            {
                line.replace(it, letters.size(), digit);
            }
        });

        std::vector<int> digits{extract_digits(line)};
        ans += 10 * digits.front() + digits.back();
    });

    std::cout << "Part 2: " << ans << std::endl;
}

int main()
{
    solve_part_one();
    solve_part_two();
}
