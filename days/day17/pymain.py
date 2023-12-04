import time

from utilities.pyutils import *
import sys
sys.path.append("/home/emergency/advent-of-code/")


start = time.time()

"""
function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
"""

symbol = \
    {
        (1, 0): 'v',
        (-1, 0): '^',
        (0, -1): '<',
        (0, 1): '>',
    }


def go_deep(grid, y1, x1, path, spath, score, best_score):

    # s = ''.join([symbol[(p2[0]-p1[0], p2[1]-p1[1])]
    #             for p1, p2 in zip(path[:-1], path[1:])])
    # print(f"{spath:100s}", end='\r')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in path:
                print('X', end='')
            else:
                print('.', end='')
        print()
    print('\n\n\n\n\n')

    # print("-"*len(path))
    # print(f"{len(path):4d}, score={score:4d}, position=({y1:3d}, {x1:3d})", end='\r')

    # print()
    # print()
    # for i in range(len(grid)):
    #     s = ""
    #     for j in range(len(grid[i])):
    #         if (i ,j) in path:
    #             s += 'x'
    #         else:
    #             s += '.'
    #     print(s)

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        y2, x2 = y1 + dy, x1 + dx

        if (y2, x2) in path:
            continue

        if not (0 <= y2 < len(grid) and 0 <= x2 < len(grid[0])):
            continue

        # avoid to go back
        if len(path) > 1:
            if (y2, x2) == path[-2]:
                continue

        if len(path) > 4:
            (y_0, y_1, y_2, y_3), y_4 = [path[i][0] for i in range(-4, 0)], y2
            (x_0, x_1, x_2, x_3), x_4 = [path[i][1] for i in range(-4, 0)], x2

            if (y_1-y_0 == y_2-y_1 == y_3-y_2 == y_4-y_3) and (x_1-x_0 == x_2-x_1 == x_3-x_2 == x_4-x_3):
                continue

        # if len(path) > 5:
            #     spath = ''.join([symbol[(p2[0]-p1[0], p2[1]-p1[1])]
            #                     for p1, p2 in zip((path + [(y2, x2)])[:-1], (path + [(y2, x2)])[1:])])
            #     # print(f"path: {path}, spath: {spath}")
            if spath[-6:] in ["^>>^>v", "v>>^>v",
                              "^>>v>^", "v>>v>^",
                              ">vv<v>", "<vv<v>",
                              ">vv>v<", "<vv>v<",
                              ">^^<^>", "<^^<^>",
                              ">^^>^<", "<^^>^<",
                              "^<<^<v", "v<<^<v",
                              "^<<v<^", "v<<v<^"]:
                #         # print("gop")
                continue

        new_score = score + grid[y2][x2]
        if new_score > best_score:
            continue

        if (y2, x2) == (len(grid)-1, len(grid[0])-1):
            best_score = min(new_score, best_score)
            # print(path + [(y2, x2)], best_score)
            # s = ''.join([symbol[(p2[0]-p1[0], p2[1]-p1[1])] for p1, p2 in zip(
            #     (path + [(y2, x2)])[:-1], (path + [(y2, x2)])[1:])]) + f" {best_score}"
            print(
                f"{spath + symbol[(y2-y1, x2-x1)]:100s} {best_score:4d} - time: {time.time() - start: 8.4f}", end='\n')
            continue

        best_score = go_deep(grid, y2, x2, list(path + [(y2, x2)]), spath + symbol[(y2-y1, x2-x1)], new_score, best_score)  # noqa

    return best_score


"""
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = 1e7
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
"""


def min_distance(dist, sptSet, num_vertices):
    min = 1e7

    for v in range(num_vertices):
        if dist[v] <= min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index


def is_connected(u, v, h, w):
    uy, ux = u // w, u % w
    vy, vx = v // w, v % w

    return abs(uy-vy) + abs(ux-vx) == 1


def get_weight(grid, u, v, h, w, prev):
    vy, vx = v // w, v % w

    d = v
    c = u
    b = prev[u]
    if b is None:
        return grid[vy][vx]
    a = prev[b]
    if a is None:
        return grid[vy][vx]

    ay, ax = a // w, a % w
    by, bx = b // w, b % w
    cy, cx = c // w, c % w
    dy, dx = d // w, d % w

    penality = 0
    if (dy-cy == cy-by == by-ay) and (dx-cx == cx-bx == bx-ax):
        penality = 1000

    return grid[vy][vx] + penality


def there_are_three_steps_in_the_same_direction(u, v, prev, h, w):
    try:
        a, b, c, d, e = prev[prev[prev[u]]], prev[prev[u]], prev[u], u, v
    except TypeError:
        return False

    if None in [a, b, c, d, e]:
        return False

    ay, ax = a // w, a % w
    by, bx = b // w, b % w
    cy, cx = c // w, c % w
    dy, dx = d // w, d % w
    ey, ex = e // w, e % w

    return (ey-dy == dy-cy == cy-by == by-ay) and (ex-dx == dx-cx == cx-bx == bx-ax)


def dijkstra(grid, source):
    h, w = len(grid), len(grid[0])
    num_vertices = h * w

    dist = [1e7] * num_vertices
    prev = [None] * num_vertices
    dist[source] = 0
    sptSet = [False] * num_vertices

    for cout in range(num_vertices):
        u = min_distance(dist, sptSet, num_vertices)

        sptSet[u] = True

        for v in range(num_vertices):
            # if there_are_three_steps_in_the_same_direction(u, v, prev, h, w):
            #     continue
            if is_connected(u, v, h, w) and sptSet[v] == False and dist[v] > dist[u] + get_weight(grid, u, v, h, w, prev):
                dist[v] = dist[u] + get_weight(grid, u, v, h, w, prev)
                prev[v] = u

    return dist, prev


def solve_part_one():
    grid = read_input_test(day=17, delimiter='\n')
    grid = [list(map(int, line)) for line in grid]

    dist, prev = dijkstra(grid, 0)

    # for line in grid:
    #     print(line)

    # print(prev)

    path = []
    pos = len(prev) - 1
    while pos != 0:
        path.append((pos // len(grid[0]), pos % len(grid[0])))
        pos = prev[pos]
    path.append((pos // len(grid[0]), pos % len(grid[0])))

    print(path[::-1])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in path:
                print('x', end='')
            else:
                print('.', end='')
        print()

    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         print(f"{dist[i*len(grid[0])+j]:4d}", end='')
    #     print()

    # best_score = go_deep(grid, 0, 0, [(0, 0)], "", 0, int(1e7))

    # for line in best_score:
    #     print(''.join([f"{i:4}" for i in line]))

    ans = 0
    print(f"part 1: {ans}")


def solve_part_two():
    grid = read_input(day=17, delimiter='\n')
    ans = 0
    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
