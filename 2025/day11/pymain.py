from utilities.pyutils import *
from collections import defaultdict


def parse_content(content):
    lines = [line.split(":") for line in content.split("\n")]
    inouts = {line[0]: line[1].strip().split(" ") for line in lines}
    return inouts


def solve_part_one(content):
    timer = Timer()

    inouts = parse_content(content)

    path_count = defaultdict(int, {"you": 1})

    # standard BFS
    queue = ["you"]
    visited = set()

    while queue:
        current = queue.pop(0)

        if current in visited:
            continue
        visited.add(current)

        if current in inouts:
            for next_node in inouts[current]:
                path_count[next_node] += path_count[current]

                # continue until we reach the end node
                if next_node not in visited and next_node != "out":
                    queue.append(next_node)

    ans = path_count.get("out", 0)
    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    inouts = parse_content(content)

    node_fft = "fft"
    node_dac = "dac"

    # this takes track of how many paths that go through a specific node (none, fft, dac, both) are reachable from node `node`.
    # counts[node] = [count_none, count_seen_fft, count_seen_dac, count_seen_both]
    init_counts = lambda node: counts.setdefault(node, [0, 0, 0, 0])
    counts = {}

    # initialize at start 'svr'
    init_counts("svr")

    # no fft or dac node has been observed in any path reachable by svr
    counts["svr"][0] = 1

    # build adjacency list and compute in-degrees
    adj = defaultdict(list)
    indeg = defaultdict(int)

    for current in inouts:
        for next_node in inouts[current]:
            adj[current].append(next_node)
            indeg[next_node] += 1

    topo_queue = [node for node in inouts if indeg[node] == 0]

    # move the `svr` at the beginning so it is processed first (Khan's algo)
    topo_queue.remove("svr")
    topo_queue.insert(0, "svr")

    while topo_queue:
        current = topo_queue.pop(0)
        if current not in adj:
            continue

        c_none, c_a, c_b, c_both = counts[current]

        for next_node in adj[current]:
            init_counts(next_node)

            if next_node == node_fft:
                counts[next_node][1] += c_none
                counts[next_node][3] += c_b
                counts[next_node][1] += counts[current][1]
                counts[next_node][3] += c_both
            elif next_node == node_dac:
                counts[next_node][2] += c_none
                counts[next_node][3] += c_a
                counts[next_node][2] += counts[current][2]
                counts[next_node][3] += c_both
            else:
                counts[next_node][0] += c_none
                counts[next_node][1] += c_a
                counts[next_node][2] += c_b
                counts[next_node][3] += c_both

            indeg[next_node] -= 1
            if indeg[next_node] == 0:
                topo_queue.append(next_node)

    ans = counts.get("out")[3]
    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day11/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
