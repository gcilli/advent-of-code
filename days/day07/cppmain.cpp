#include <algorithm>
#include <cmath>
#include <iostream>
#include <tuple>
#include <unordered_map>
#include <vector>

#include "utilities/cpputils.h"

std::uint64_t get_hand_value(const std::string& hand, bool use_j_as_jolly)
{
    std::unordered_map<char, int> card_value{
        {'2', 2},
        {'3', 3},
        {'4', 4},
        {'5', 5},
        {'6', 6},
        {'7', 7},
        {'8', 8},
        {'9', 9},
        {'T', 10},
        {'J', use_j_as_jolly ? 1 : 11},
        {'Q', 12},
        {'K', 13},
        {'A', 14},
    };

    std::uint64_t hand_value{0U};
    std::unordered_map<char, int> cards;
    for (std::size_t i{0U}; i < hand.size(); i++)
    {
        const char card{hand[i]};
        cards[card]++;
        hand_value += std::pow(16, (5 - i)) * card_value[card];
    }

    if (use_j_as_jolly && cards.contains('J') && cards['J'] != 5)
    {
        std::vector<std::pair<char, int>> cards_without_j;
        for (const auto& [card, amount] : cards)
        {
            if (card != 'J')
            {
                cards_without_j.push_back(std::make_pair(card, amount));
            }
        }

        std::sort(cards_without_j.begin(), cards_without_j.end(), [](const auto& card1, const auto& card2) {
            return card1.second > card2.second;
        });

        const auto card_in_highest_quantity = cards_without_j[0].first;
        cards[card_in_highest_quantity] += cards['J'];
        cards.extract('J');
    }

    // five of a kind
    if (cards.size() == 1)
    {
        return hand_value + std::pow(16, 12);
    }

    // either full house or four of a kind
    if (cards.size() == 2)
    {
        const auto values = utils::get_dict_values(cards);
        return hand_value + std::pow(16, *std::ranges::max_element(values) == 4 ? 11 : 10);
    }

    // either three of a kind or two pairs
    if (cards.size() == 3)
    {
        const auto values = utils::get_dict_values(cards);
        return hand_value + std::pow(16, *std::ranges::max_element(values) == 3 ? 9 : 8);
    }

    // one pair
    if (cards.size() == 4)
    {
        return hand_value + std::pow(16, 7);
    }

    // high card
    return hand_value + std::pow(16, 6);
}

std::uint64_t solve(bool use_j_as_jolly)
{
    const std::vector<std::string> content = utils::split(utils::read_input(7), "\n");

    std::vector<std::tuple<std::string, int, std::uint64_t>> hands;
    for (const auto& line : content)
    {
        const std::vector<std::string> tokens = utils::split(line, " ");
        hands.push_back({tokens[0U], std::stoi(tokens[1U]), get_hand_value(tokens[0U], use_j_as_jolly)});
    }

    std::sort(hands.begin(), hands.end(), [](const auto& hand1, const auto& hand2) {
        return std::get<2>(hand1) < std::get<2>(hand2);
    });

    std::uint64_t ans{0U};
    for (std::size_t i{0U}; i < hands.size(); i++)
    {
        ans += (i + 1) * std::get<1>(hands[i]);
    }

    return ans;
}

void solve_part_one()
{
    std::uint64_t ans = solve(false);
    std::cout << "part 1: " << ans << std::endl;
}

void solve_part_two()
{
    std::uint64_t ans = solve(true);
    std::cout << "part 2: " << ans << std::endl;
}

int main()
{
    solve_part_one();
    solve_part_two();
}
