#include "utilities/cpputils.h"

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct Point
{
    std::uint64_t x;
    std::uint64_t y;

    bool operator==(const Point& other) const { return x == other.x && y == other.y; }
};

struct PointHash
{
    std::size_t operator()(const Point& p) const
    {
        return std::hash<std::uint64_t>()(p.x) ^ (std::hash<std::uint64_t>()(p.y) << 1);
    }
};

std::vector<Point> parse_points(const std::string& content)
{
    std::vector<Point> points;
    std::stringstream ss(content);
    std::string line;

    while (std::getline(ss, line))
    {
        if (line.empty())
            continue;

        auto comma_pos = line.find(',');
        if (comma_pos != std::string::npos)
        {
            std::uint64_t x = std::stoll(line.substr(0, comma_pos));
            std::uint64_t y = std::stoll(line.substr(comma_pos + 1));
            points.push_back({x, y});
        }
    }

    return points;
}

bool point_is_in_polygon(const std::vector<Point>& polygon, const Point& point)
{
    std::uint64_t px = point.x;
    std::uint64_t py = point.y;
    std::size_t n = polygon.size();

    bool inside = false;

    // ray - casting algorithm..
    // j points to the previous vertex.So, since the first vertex
    // we consider is at position 0, the previous one is at position n - 1
    std::size_t j = n - 1;

    for (std::size_t i = 0; i < n; ++i)
    {
        std::uint64_t xi = polygon[i].x;
        std::uint64_t yi = polygon[i].y;
        std::uint64_t xj = polygon[j].x;
        std::uint64_t yj = polygon[j].y;

        // check if point is on horizontal edge
        if (yi == yj && yi == py)
        {
            if ((xi <= px && px <= xj) || (xj <= px && px <= xi))
            {
                return true;
            }
        }

        // check if point is on vertical edge
        if (xi == xj && xi == px)
        {
            if ((yi <= py && py <= yj) || (yj <= py && py <= yi))
            {
                return true;
            }
        }

        // only count vertical edges that cross our horizontal ray
        if (xi == xj)
        {
            if ((yi < py && py <= yj) || (yj < py && py <= yi))
            {
                if (xi > px)
                {
                    inside = !inside;
                }
            }
        }

        j = i;
    }

    return inside;
}

bool rectangle_inside_polygon_with_cache(const std::vector<Point>& polygon,
                                         std::uint64_t rect_min_x,
                                         std::uint64_t rect_max_x,
                                         std::uint64_t rect_min_y,
                                         std::uint64_t rect_max_y,
                                         std::unordered_map<Point, bool, PointHash>& cache,
                                         const std::vector<std::uint64_t>& unique_x,
                                         const std::vector<std::uint64_t>& unique_y)
{
    // get the x coordinates to check(only those in unique_x that fall within rect bounds)
    std::vector<std::uint64_t> x_coords_to_check;
    std::vector<std::uint64_t> y_coords_to_check;

    for (std::uint64_t x : unique_x)
    {
        if (rect_min_x <= x && x <= rect_max_x)
        {
            x_coords_to_check.push_back(x);
        }
    }

    for (std::uint64_t y : unique_y)
    {
        if (rect_min_y <= y && y <= rect_max_y)
        {
            y_coords_to_check.push_back(y);
        }
    }

    // add boundary coordinates if not present
    if (std::find(x_coords_to_check.begin(), x_coords_to_check.end(), rect_min_x) == x_coords_to_check.end())
    {
        x_coords_to_check.insert(x_coords_to_check.begin(), rect_min_x);
    }
    if (std::find(x_coords_to_check.begin(), x_coords_to_check.end(), rect_max_x) == x_coords_to_check.end())
    {
        x_coords_to_check.push_back(rect_max_x);
    }
    if (std::find(y_coords_to_check.begin(), y_coords_to_check.end(), rect_min_y) == y_coords_to_check.end())
    {
        y_coords_to_check.insert(y_coords_to_check.begin(), rect_min_y);
    }
    if (std::find(y_coords_to_check.begin(), y_coords_to_check.end(), rect_max_y) == y_coords_to_check.end())
    {
        y_coords_to_check.push_back(rect_max_y);
    }

    // check the perimeters points (here the points are at discrete coordinates):

    // check top and bottom edges
    for (std::uint64_t x : x_coords_to_check)
    {
        for (std::uint64_t y_edge : {rect_min_y, rect_max_y})
        {
            Point point{x, y_edge};
            if (cache.find(point) == cache.end())
            {
                cache[point] = point_is_in_polygon(polygon, point);
            }
            if (!cache[point])
            {
                return false;
            }
        }
    }

    // check left and right edges
    for (std::uint64_t y : y_coords_to_check)
    {
        for (std::uint64_t x_edge : {rect_min_x, rect_max_x})
        {
            Point point{x_edge, y};
            if (cache.find(point) == cache.end())
            {
                cache[point] = point_is_in_polygon(polygon, point);
            }
            if (!cache[point])
            {
                return false;
            }
        }
    }

    return true;
}

void solve_part_one(const std::string& content)
{
    utils::Timer timer;

    std::vector<Point> red_tiles = parse_points(content);

    std::int64_t max_area = 0;

    for (std::size_t i = 0; i < red_tiles.size(); ++i)
    {
        for (std::size_t j = i + 1; j < red_tiles.size(); ++j)
        {
            std::int64_t x1 = red_tiles[i].x;
            std::int64_t y1 = red_tiles[i].y;
            std::int64_t x2 = red_tiles[j].x;
            std::int64_t y2 = red_tiles[j].y;

            std::int64_t width = std::abs(x2 - x1) + 1;
            std::int64_t height = std::abs(y2 - y1) + 1;
            std::int64_t area = width * height;

            max_area = std::max(max_area, area);
        }
    }

    std::uint64_t ans = max_area;
    std::cout << "part 1 (runtime: " << timer.elapsed_ms() << "ms): " << ans << std::endl;
}

void solve_part_two(const std::string& content)
{
    utils::Timer timer;

    std::vector<Point> polygon = parse_points(content);

    // close the polygon
    polygon.push_back(polygon[0]);

    // pre-cache polygon bounding box
    std::uint64_t poly_min_x = polygon[0].x;
    std::uint64_t poly_max_x = polygon[0].x;
    std::uint64_t poly_min_y = polygon[0].y;
    std::uint64_t poly_max_y = polygon[0].y;
    for (const auto& p : polygon)
    {
        poly_min_x = std::min(poly_min_x, p.x);
        poly_max_x = std::max(poly_max_x, p.x);
        poly_min_y = std::min(poly_min_y, p.y);
        poly_max_y = std::max(poly_max_y, p.y);
    }

    // extract unique x and y coordinates
    std::unordered_set<std::uint64_t> unique_x_set, unique_y_set;
    for (const auto& p : polygon)
    {
        unique_x_set.insert(p.x);
        unique_y_set.insert(p.y);
    }

    std::vector<std::uint64_t> unique_x(unique_x_set.begin(), unique_x_set.end());
    std::vector<std::uint64_t> unique_y(unique_y_set.begin(), unique_y_set.end());
    std::sort(unique_x.begin(), unique_x.end());
    std::sort(unique_y.begin(), unique_y.end());

    // cache for point checks
    std::unordered_map<Point, bool, PointHash> point_cache;

    std::uint64_t max_area = 0;
    std::size_t n = polygon.size() - 1;
    for (std::size_t i = 0; i < n; ++i)
    {
        Point p1 = polygon[i];

        for (std::size_t j = i + 1; j < n; ++j)
        {
            Point p2 = polygon[j];

            std::uint64_t min_x = std::min(p1.x, p2.x);
            std::uint64_t max_x = std::max(p1.x, p2.x);
            std::uint64_t min_y = std::min(p1.y, p2.y);
            std::uint64_t max_y = std::max(p1.y, p2.y);

            std::uint64_t height = max_y - min_y + 1;
            std::uint64_t width = max_x - min_x + 1;
            std::uint64_t area = height * width;

            // check the area of the polygon.
            // if it's smaller than the biggest found so far, we can exclude it
            if (area <= max_area)
            {
                continue;
            }

            // check if rectangle is within polygon bbox. If not, skip it
            if (min_x < poly_min_x || max_x > poly_max_x || min_y < poly_min_y || max_y > poly_max_y)
            {
                continue;
            }

            if (rectangle_inside_polygon_with_cache(
                    polygon, min_x, max_x, min_y, max_y, point_cache, unique_x, unique_y))
            {
                max_area = area;
            }
        }
    }

    std::cout << "part 2 (runtime: " << timer.elapsed_ms() << "ms): " << max_area << std::endl;
}

int main()
{
    const std::string content = utils::read_file("2025/day09/inputs/input.txt");

    solve_part_one(content);
    solve_part_two(content);
}
