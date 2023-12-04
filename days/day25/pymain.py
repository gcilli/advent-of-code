from utilities.pyutils import *


def solve_part_one():
    content = read_input(day=24, delimiter='\n')

    positions = []
    velocities = []
    for line in content:
        tokens = line.split('@')
        positions.append(tuple(map(int, tokens[0].split(','))))
        velocities.append(tuple(map(int, tokens[1].split(','))))

    # limit = (7, 27)
    limit = (200000000000000, 400000000000000)

    paths_eq = []
    for pos, vel in zip(positions, velocities):
        px, py, pz = pos
        vx, vy, vz = vel

        m = vy / vx
        q = py - m*px

        paths_eq.append((m, q))

    ans = 0
    for i in range(len(content)):
        for j in range(i, len(content)):
            m1, q1 = paths_eq[i]
            m2, q2 = paths_eq[j]

            if m1 == m2:
                continue

            px = (q2-q1)/(m1-m2)
            py = m1*(q2-q1)/(m1-m2)+q1

            if not (limit[0] <= px <= limit[1] and limit[0] <= py <= limit[1]):
                print(f"cross {px:.2f}, {py:.2f} occurred outside limit area")
                continue

            # check if the cross occurred in the past
            px0, py0, pz0 = positions[i]
            vx0, vy0, vz0 = velocities[i]
            t0 = (px - px0) / vx0

            px1, py1, pz1 = positions[j]
            vx1, vy1, vz1 = velocities[j]
            t1 = (px - px1) / vx1

            if t0 < 0 or t1 < 0:
                print(
                    f"cross {px:.2f}, {py:.2f} occurred in the past: {t0:.2f} and {t1:.2f}")
                continue
            else:
                print(f"{px:.2f}, {py:.2f}")

            ans += 1

    print(f"part 1: {ans}")


def solve_part_two():
    grid = read_input_test(day=24, delimiter='\n')

    ans = 0
    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()  # takes hours :D
