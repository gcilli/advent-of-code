import math

from utilities.pyutils import *


def solve_part_one():
    cmds, content = read_input(day=8, delimiter='\n\n')
    nodes = {line[:3]: (line[7:10], line[12:15])
             for line in content.split('\n')}

    ans = 0
    node = "AAA"
    while node != "ZZZ":
        cmd = cmds[ans % len(cmds)]
        node = nodes[node][cmd == 'R']
        ans += 1

    print(f"part 1: {ans}")


def solve_part_two():
    cmds, content = read_input(day=8, delimiter='\n\n')
    nodes = {line[:3]: (line[7:10], line[12:15])
             for line in content.split('\n')}

    ans = 0

    all_steps = []
    starting_nodes = [i for i in nodes.keys() if i.endswith('A')]
    for node in starting_nodes:
        steps = 0
        while not node.endswith('Z'):
            cmd = cmds[steps % len(cmds)]
            node = nodes[node][cmd == 'R']
            steps += 1
        all_steps.append(steps)

    ans = math.lcm(*all_steps)
    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
