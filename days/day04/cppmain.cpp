#include <algorithm>
#include <cmath>
#include <iostream>
#include <unordered_map>

#include "utilities/cpputils.h"

std::pair<std::vector<std::vector<int>>, std::vector<std::vector<int>>> parse_input()
{
    std::vector<std::vector<std::string>> content;
    std::ranges::for_each(utils::split(utils::read_input(4), "\n"), [&content](const std::string& line) {
        content.push_back(utils::split(utils::split(line, ":")[1], "|"));
    });

    std::vector<std::vector<std::uint64_t>> win_cards;
    std::vector<std::vector<std::uint64_t>> my_cards;
    std::ranges::for_each(content, [&win_cards, &my_cards](const auto& game) {
        win_cards.push_back(utils::get_vector_of_numbers(game[0], " "));
        my_cards.push_back(utils::get_vector_of_numbers(game[1], " "));
    });

    return {win_cards, my_cards};
}

void solve_part_one()
{
    auto [win_cards, my_cards] = parse_input();

    std::uint32_t ans{0U};
    for (std::size_t i{0U}; i < win_cards.size(); i++)
    {
        const auto& game_win_cards = win_cards[i];
        const auto& game_my_cards = my_cards[i];
        std::uint32_t num_winning_cards = 0U;
        std::ranges::for_each(game_win_cards, [&game_my_cards, &num_winning_cards](const int card) {
            if (std::ranges::find(game_my_cards, card) != game_my_cards.cend())
            {
                num_winning_cards++;
            }
        });
        ans += num_winning_cards ? ::pow(2, num_winning_cards - 1) : 0;
    }

    std::cout << "part 1: " << ans << std::endl;
}

void solve_part_two()
{
    auto [win_cards, my_cards] = parse_input();

    std::unordered_map<int, int> copies;
    for (std::size_t i{0U}; i < win_cards.size(); i++)
    {
        copies[i] = 1;
    }

    for (std::size_t i{0U}; i < win_cards.size(); i++)
    {
        const auto& game_win_cards = win_cards[i];
        const auto& game_my_cards = my_cards[i];
        std::uint32_t num_winning_cards = 0U;
        std::ranges::for_each(game_win_cards, [&game_my_cards, &num_winning_cards](const int card) {
            if (std::ranges::find(game_my_cards, card) != game_my_cards.cend())
            {
                num_winning_cards++;
            }
        });
        for (std::size_t j{i + 1U}; j < i + 1U + num_winning_cards; j++)
        {
            copies[j] += copies[i];
        }
    }

    std::uint32_t ans{0U};
    std::ranges::for_each(copies, [&ans](const auto& key_value) { ans += key_value.second; });

    std::cout << "part 2: " << ans << std::endl;
}

int main()
{
    solve_part_one();
    solve_part_two();
}
