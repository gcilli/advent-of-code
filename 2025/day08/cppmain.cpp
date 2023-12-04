#include "utilities/cpputils.h"

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

struct Junction
{
    int x;
    int y;
    int z;

    bool operator==(const Junction& other) const { return x == other.x && y == other.y && z == other.z; }
};

struct JunctionHash
{
    std::size_t operator()(const Junction& j) const
    {
        return std::hash<int>()(j.x) ^ (std::hash<int>()(j.y) << 1) ^ (std::hash<int>()(j.z) << 2);
    }
};

int64_t get_distance(const Junction& j1, const Junction& j2)
{
    int64_t dx = j1.x - j2.x;
    int64_t dy = j1.y - j2.y;
    int64_t dz = j1.z - j2.z;
    return dx * dx + dy * dy + dz * dz;
}

struct Edge
{
    Junction j1;
    Junction j2;
    int64_t distance;
};

std::vector<Junction> parse_content(const std::string& content)
{
    std::vector<Junction> junctions;
    std::stringstream ss(content);
    std::string line;
    while (std::getline(ss, line))
    {
        if (line.empty())
            continue;

        std::stringstream ls(line);
        std::string val;
        std::vector<int> values;
        while (std::getline(ls, val, ','))
        {
            values.push_back(std::stoi(val));
        }

        if (values.size() >= 3)
        {
            junctions.push_back({values[0], values[1], values[2]});
        }
    }

    return junctions;
}

int64_t connect(const std::vector<Junction>& junctions, std::optional<int> max_connections)
{
    std::vector<Edge> distances;
    for (size_t i = 0; i < junctions.size(); ++i)
    {
        for (size_t j = i + 1; j < junctions.size(); ++j)
        {
            distances.push_back({junctions[i], junctions[j], get_distance(junctions[i], junctions[j])});
        }
    }

    // sort all edges by distance
    std::sort(distances.begin(), distances.end(), [](const Edge& a, const Edge& b) { return a.distance < b.distance; });

    // find circuits using junctions as keys
    std::unordered_map<Junction, int, JunctionHash> circuits;
    int circuit_id = 0;

    int connections = (!max_connections.has_value())
                          ? static_cast<int>(distances.size())
                          : std::min(max_connections.value(), static_cast<int>(distances.size()));

    for (int i = 0; i < connections; ++i)
    {
        Junction j1 = distances[i].j1;
        Junction j2 = distances[i].j2;

        bool j1_in = circuits.count(j1) > 0;
        bool j2_in = circuits.count(j2) > 0;

        if (j1_in && j2_in)
        {
            // same circuit, do nothing
            if (circuits[j1] == circuits[j2])
            {
                continue;
            }

            // merge circuits
            int min_cid = std::min(circuits[j1], circuits[j2]);
            int max_cid = std::max(circuits[j1], circuits[j2]);
            circuits[j1] = min_cid;
            circuits[j2] = min_cid;

            for (auto& [node, cid] : circuits)
            {
                if (cid == max_cid)
                {
                    cid = min_cid;
                }
            }
        }
        else if (j1_in && !j2_in)
        {
            circuits[j2] = circuits[j1];
        }
        else if (!j1_in && j2_in)
        {
            circuits[j1] = circuits[j2];
        }
        else
        {
            // new circuit
            circuits[j1] = circuit_id;
            circuits[j2] = circuit_id;
            circuit_id++;
        }

        // part 2: check if all junctions connected
        if (!max_connections.has_value() && circuits.size() == junctions.size())
        {
            return static_cast<int64_t>(j1.x) * j2.x;
        }
    }

    // part 1: return product of three largest circuits
    if (max_connections.has_value())
    {
        std::unordered_map<int, int> circuit_sizes;
        for (const auto& [node, cid] : circuits)
        {
            circuit_sizes[cid]++;
        }

        std::vector<int> sizes;
        for (const auto& [cid, size] : circuit_sizes)
        {
            sizes.push_back(size);
        }
        std::sort(sizes.rbegin(), sizes.rend());

        if (sizes.size() >= 3)
        {
            return static_cast<int64_t>(sizes[0]) * sizes[1] * sizes[2];
        }
    }

    return 0;
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    const std::vector<Junction> junctions = parse_content(content);

    int64_t ans = connect(junctions, 1000);

    std::cout << std::format("Part 1 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    const std::vector<Junction> junctions = parse_content(content);

    int64_t ans = connect(junctions, std::nullopt);

    std::cout << std::format("Part 2 (runtime: {:.3f}ms): {}", timer.elapsed_ms(), ans) << std::endl;
}

int main()
{
    const std::string content = utils::read_file("2025/day08/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
