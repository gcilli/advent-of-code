#ifndef UTILITIES_H
#define UTILITIES_H

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

namespace utils
{

std::string read_input(const int day);
std::string read_input_test(const int day);
std::vector<std::string> split(const std::string& s, const std::string& d);
std::vector<std::string> pad_grid(const std::vector<std::string>& grid, const int pad_width, const char filler);
std::vector<std::uint64_t> get_vector_of_numbers(const std::string& s, const std::string& del);
template <typename KeyT, typename ValueT>
std::vector<ValueT> get_dict_values(std::unordered_map<KeyT, ValueT> map);

}  // namespace utils

#endif
