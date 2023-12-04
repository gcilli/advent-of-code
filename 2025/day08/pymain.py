from utilities.pyutils import *


def parse_content(content):
    junctions = [tuple(map(int, line.split(","))) for line in content.split("\n")]
    return junctions


def get_distance(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2))


def connect(junctions, max_connections=None):
    distances = [
        (junctions[i], junctions[j], get_distance(junctions[i], junctions[j]))
        for i in range(len(junctions))
        for j in range(i + 1, len(junctions))
    ]

    distances.sort(key=lambda x: x[2])

    circuits = {}
    circuit_id = 0
    for i in range(max_connections if max_connections is not None else len(distances)):
        j1, j2, _ = distances[i]

        if j1 in circuits and j2 in circuits:
            # same circuits, nothing happens
            if circuits[j1] == circuits[j2]:
                continue

            # different circuits, merge
            if circuits[j1] != circuits[j2]:
                cid = min(circuits[j1], circuits[j2])
                max_cid = max(circuits[j1], circuits[j2])
                circuits[j1] = cid
                circuits[j2] = cid

                for c in circuits:
                    if circuits[c] == max_cid:
                        circuits[c] = cid

        elif j1 in circuits and j2 not in circuits:
            # add j2 to j1's circuit
            circuits[j2] = circuits[j1]

        elif j1 not in circuits and j2 in circuits:
            # add j1 to j2's circuit
            circuits[j1] = circuits[j2]

        else:
            # new circuit
            circuits[j1] = circuit_id
            circuits[j2] = circuit_id
            circuit_id += 1

        # part 2
        if len(circuits) == len(junctions):
            # all junctions connected
            return j1[0] * j2[0]

    # part 1
    if max_connections is not None:
        n_circuits = max(circuits.values()) + 1
        circuits_size = [0] * n_circuits
        for cid in circuits.values():
            circuits_size[cid] += 1
        s1, s2, s3 = sorted(circuits_size, reverse=True)[:3]
        return s1 * s2 * s3


def solve_part_one(content):
    timer = Timer()

    junctions = parse_content(content)
    ans = connect(junctions, max_connections=1000)

    print(f"part 1 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


def solve_part_two(content):
    timer = Timer()

    junctions = parse_content(content)
    ans = connect(junctions)

    print(f"part 2 (runtime: {timer.elapsed_ms():.3f}ms): {ans}")


if __name__ == "__main__":
    content = read_input("2025/day08/inputs/input.txt")

    solve_part_one(content)
    solve_part_two(content)
