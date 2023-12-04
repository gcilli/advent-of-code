#include <iostream>
#include <regex>
#include <unordered_map>

#include "utilities/cpputils.h"

void solve_part_one()
{
    const std::vector<std::string> content{utils::split(utils::read_input(8), "\n\n")};

    std::string cmds = content[0];
    cmds.pop_back();
    std::unordered_map<std::string, std::pair<std::string, std::string>> nodes;
    for (const std::string& line : utils::split(content[1], "\n"))
    {
        std::string node{line.cbegin(), line.cbegin() + 3};
        std::string left{line.cbegin() + 7, line.cbegin() + 10};
        std::string right{line.cbegin() + 12, line.cbegin() + 15};
        nodes[node] = {left, right};
    }

    std::uint32_t ans{0U};
    std::string node{"AAA"};
    while (node != "ZZZ")
    {
        char cmd = cmds[(ans % cmds.size())];
        node = (cmd == 'L') ? nodes[node].first : nodes[node].second;
        ans++;
    }

    std::cout << "Part 1: " << ans << std::endl;
}

void solve_part_two()
{
    // const std::vector<std::string> content{utils::split(utils::read_input(2), '\n')};
    std::uint32_t ans{0U};
    std::cout << "Part 2: " << ans << std::endl;
}

int main()
{
    solve_part_one();
    solve_part_two();
}
