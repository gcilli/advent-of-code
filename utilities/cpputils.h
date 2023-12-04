#ifndef UTILITIES_H
#define UTILITIES_H

#include <ranges>

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

namespace utils
{

class Timer
{
  public:
    Timer() : start_(std::chrono::high_resolution_clock::now()) {}

    void reset() { start_ = std::chrono::high_resolution_clock::now(); }

    double elapsed_ms() const
    {
        auto end = std::chrono::high_resolution_clock::now();
        return std::chrono::duration<double, std::milli>(end - start_).count();
    }

  private:
    std::chrono::time_point<std::chrono::high_resolution_clock> start_;
};

std::string read_file(const std::string& path)
{
    std::ifstream istream{path};
    if (!istream.is_open())
    {
        std::cerr << "Error: Could not open file: " << path << std::endl;
        return "";
    }
    std::stringstream buffer;
    buffer << istream.rdbuf();
    return buffer.str();
}

auto split(const std::string& str, std::string_view del)
{
    return str | std::views::split(del) | std::views::transform([](auto&& rng) {
               return std::string_view(&*rng.begin(), std::ranges::distance(rng));
           });
}

}  // namespace utils

#endif
