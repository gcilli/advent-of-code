#include "utilities/cpputils.h"

#include <format>
#include <ranges>

#include <algorithm>
#include <array>
#include <deque>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using Graph = std::unordered_map<std::string, std::vector<std::string>>;

Graph parse_content(const std::string& content)
{
    Graph inouts;
    std::stringstream ss(content);
    std::string line;

    while (std::getline(ss, line))
    {
        if (line.empty())
            continue;

        auto colon_pos = line.find(':');
        if (colon_pos != std::string::npos)
        {
            const std::string node = line.substr(0, colon_pos);
            std::string destinations = line.substr(colon_pos + 1);

            const size_t start = destinations.find_first_not_of(' ');
            if (start != std::string::npos)
            {
                destinations = destinations.substr(start);
            }

            std::stringstream dest_ss(destinations);
            std::string dest;
            while (dest_ss >> dest)
            {
                inouts[node].push_back(dest);
            }
        }
    }

    return inouts;
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    Graph inouts = parse_content(content);

    std::unordered_map<std::string, std::uint64_t> path_count;
    path_count["you"] = 1;

    // standard BFS
    std::deque<std::string> queue = {"you"};
    std::unordered_set<std::string> visited;

    while (!queue.empty())
    {
        const std::string current = queue.front();
        queue.pop_front();

        if (visited.contains(current))
            continue;
        visited.insert(current);

        if (inouts.contains(current))
        {
            for (const auto& next_node : inouts[current])
            {
                path_count[next_node] += path_count[current];

                // continue until we reach the end node
                if (!visited.contains(next_node) && next_node != "out")
                {
                    queue.push_back(next_node);
                }
            }
        }
    }

    std::uint64_t ans = path_count["out"];
    std::cout << std::format("part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    Graph inouts = parse_content(content);

    const std::string node_fft = "fft";
    const std::string node_dac = "dac";

    // this takes track of how many paths that go through a specific node (none, fft, dac, both) are reachable from node
    // `node`. counts[node] = [count_none, count_seen_fft, count_seen_dac, count_seen_both]
    std::unordered_map<std::string, std::array<std::uint64_t, 4>> counts;

    auto init_counts = [&](const std::string& node) {
        if (!counts.contains(node))
        {
            counts[node] = {0, 0, 0, 0};
        }
    };

    // initialize at start 'svr'
    init_counts("svr");

    // no fft or dac node has been observed in any path reachable by svr
    counts["svr"][0] = 1;

    // build adjacency list and compute in-degrees
    std::unordered_map<std::string, std::vector<std::string>> adj;
    std::unordered_map<std::string, int> indeg;

    for (const auto& [current, neighbors] : inouts)
    {
        for (const auto& next_node : neighbors)
        {
            adj[current].push_back(next_node);
            indeg[next_node]++;
        }
    }

    std::deque<std::string> topo_queue;
    for (const auto& [node, _] : inouts)
    {
        if (indeg[node] == 0)
        {
            topo_queue.push_back(node);
        }
    }

    // move the `svr` at the beginning so it is processed first (Khan's algo)
    auto svr_it = std::find(topo_queue.begin(), topo_queue.end(), "svr");
    if (svr_it != topo_queue.end())
    {
        topo_queue.erase(svr_it);
        topo_queue.push_front("svr");
    }

    while (!topo_queue.empty())
    {
        const std::string current = topo_queue.front();
        topo_queue.pop_front();

        if (!adj.contains(current))
            continue;

        const std::uint64_t c_none = counts[current][0];
        const std::uint64_t c_a = counts[current][1];
        const std::uint64_t c_b = counts[current][2];
        const std::uint64_t c_both = counts[current][3];

        for (const auto& next_node : adj[current])
        {
            init_counts(next_node);

            if (next_node == node_fft)
            {
                counts[next_node][1] += c_none;
                counts[next_node][3] += c_b;
                counts[next_node][1] += counts[current][1];
                counts[next_node][3] += c_both;
            }
            else if (next_node == node_dac)
            {
                counts[next_node][2] += c_none;
                counts[next_node][3] += c_a;
                counts[next_node][2] += counts[current][2];
                counts[next_node][3] += c_both;
            }
            else
            {
                counts[next_node][0] += c_none;
                counts[next_node][1] += c_a;
                counts[next_node][2] += c_b;
                counts[next_node][3] += c_both;
            }

            indeg[next_node]--;
            if (indeg[next_node] == 0)
            {
                topo_queue.push_back(next_node);
            }
        }
    }

    std::uint64_t ans = counts["out"][3];
    std::cout << std::format("part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    std::string content = utils::read_file("2025/day11/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
