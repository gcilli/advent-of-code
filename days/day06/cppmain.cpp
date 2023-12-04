#include <cmath>
#include <iostream>
#include <vector>

#include "utilities/cpputils.h"

void solve_part_one()
{
    const std::vector<std::string> content = utils::split(utils::read_input(6), "\n");

    const auto times = utils::get_vector_of_numbers(utils::split(content[0], ":")[1], " ");
    const auto distances = utils::get_vector_of_numbers(utils::split(content[1], ":")[1], " ");

    std::uint64_t ans{1U};
    for (std::size_t i{0U}; i < times.size(); i++)
    {
        const auto& t{times[i]};
        const auto& d{distances[i]};

        double s1 = 0.5 * (t - std::sqrt(std::pow(t, 2) - 4U * d));
        double s2 = 0.5 * (t + std::sqrt(std::pow(t, 2) - 4U * d));

        // take values inside the range only.
        std::uint64_t s1i = static_cast<std::uint64_t>(s1) + 1U;
        std::uint64_t s2i = static_cast<std::uint64_t>(s2) - (s2 - static_cast<std::uint64_t>(s2) < 0.0001);

        ans *= s2i - s1i + 1U;
    }

    std::cout << "part 1: " << ans << std::endl;
}

void solve_part_two()
{
    const std::vector<std::string> content = utils::split(utils::read_input(6), "\n");

    const auto times = utils::split(utils::split(content[0], ":")[1], " ");
    const auto distances = utils::split(utils::split(content[1], ":")[1], " ");

    std::string ts = "";
    for (const auto& time : times)
    {
        ts += time;
    }
    const std::uint64_t t = std::stoll(ts);

    std::string ds = "";
    for (const auto& distance : distances)
    {
        ds += distance;
    }
    const std::uint64_t d = std::stoll(ds);

    double s1 = 0.5 * (t - std::sqrt(std::pow(t, 2) - 4U * d));
    double s2 = 0.5 * (t + std::sqrt(std::pow(t, 2) - 4U * d));

    // take values inside the range only.
    std::uint64_t s1i = static_cast<std::uint64_t>(s1) + 1U;
    std::uint64_t s2i = static_cast<std::uint64_t>(s2) - (s2 - static_cast<std::uint64_t>(s2) < 0.0001);

    std::uint64_t ans = s2i - s1i + 1;
    std::cout << "part 2: " << ans << std::endl;
}

int main()
{
    solve_part_one();
    solve_part_two();
}
