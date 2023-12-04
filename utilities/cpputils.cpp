#include "cpputils.h"

#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <ranges>

namespace utils
{

namespace
{

std::string pad_number(const int num, const int width, const char pad)
{
    std::ostringstream ss;
    ss << std::setw(width) << std::setfill(pad) << num;
    return ss.str();
}

std::string read_file(const std::string& path)
{
    std::ifstream istream{path};
    std::stringstream buffer;
    buffer << istream.rdbuf();
    return buffer.str();
}

}  // namespace

std::string read_input(const int day)
{
    std::string padded_day{pad_number(day, 2, '0')};
    return read_file("days/day" + padded_day + "/input.txt");
}

std::string read_input_test(const int day)
{
    std::string padded_day{pad_number(day, 2, '0')};
    return read_file("days/day" + padded_day + "/input_test.txt");
}

std::vector<std::string> split(const std::string& str, const std::string& del)
{
    // clang-format off
    auto view = 
        str
        | std::views::split(del)
        | std::views::filter([](auto&& rng){return std::ranges::distance(rng) > 0;})
        | std::views::transform([](auto&& rng) -> std::string {
            return {&*rng.begin(), static_cast<std::string::size_type>(std::ranges::distance(rng))};
            });
    // clang-format on

    return {view.begin(), view.end()};
}

std::vector<std::string> pad_grid(const std::vector<std::string>& grid, const int pad_width, const char filler)
{
    std::vector<std::string> padded_grid{};

    const std::size_t height = grid.size();
    if (height == 0)
    {
        std::cout << "grid is empty." << std::endl;
        return padded_grid;
    }
    const std::size_t width = grid[0].size();

    padded_grid.emplace_back(width + pad_width * 2, filler);
    for (const auto& line : grid)
    {
        padded_grid.push_back(std::string(pad_width, filler) + line + std::string(pad_width, filler));
    }
    padded_grid.emplace_back(width + pad_width * 2, filler);

    return padded_grid;
}

std::vector<std::uint64_t> get_vector_of_numbers(const std::string& s, const std::string& del)
{
    std::vector<std::uint64_t> out;
    std::ranges::for_each(split(s, del), [&out](const std::string& token) { out.push_back(std::stoull(token)); });
    return out;
}

template <typename KeyT, typename ValueT>
std::vector<ValueT> get_dict_values(std::unordered_map<KeyT, ValueT> map)
{
    std::vector<ValueT> v;
    for (const auto& [key, value] : map)
    {
        v.push_back(value);
    }
    return v;
}

template std::vector<int> get_dict_values(std::unordered_map<char, int> map);

}  // namespace utils
