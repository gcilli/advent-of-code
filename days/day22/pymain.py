from utilities.pyutils import *


class Brick:
    def __init__(self, id, x0, y0, z0, x1, y1, z1):
        self.id = id
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

        self.landed = True if z0 == 1 else False
        self.supported_by = set()
        self.support = set()

    def set_z(self, z0, z1):
        self.z0 = z0
        self.z1 = z1

    def __iter__(self):
        return iter(((self.x0, self.y0, self.z0), (self.x1, self.y1, self.z1)))


def fall(bricks):
    falls = 0

    # do not stop until all bricks have stop falling
    while not all([b.landed for b in bricks]):
        bricks.sort(key=lambda b: b.z0)

        # during each iteration, evaluate each brick
        for i, brick0 in enumerate(bricks):

            # get the X and Y coordinates that the brick touches
            x0coords = set(list(range(brick0.x0, brick0.x1+1)))
            y0coords = set(list(range(brick0.y0, brick0.y1+1)))

            # if the brick has already stopped, skip it
            if brick0.landed:
                continue

            # iterate throught the other bricks, starting from the one below and proceeding down to z=1
            for brick1 in sorted([b for b in bricks if b.z1 < brick0.z0], key=lambda b: b.z1, reverse=True):

                # get the X and Y coordinates of the brick below
                x1coords = set(list(range(brick1.x0, brick1.x1+1)))
                y1coords = set(list(range(brick1.y0, brick1.y1+1)))

                # check if the brick below collides with the current brick along the X and Y axes
                if len(set(x0coords).intersection(x1coords)) > 0 and len(set(y0coords).intersection(y1coords)) > 0:
                    if not brick0.landed:
                        # if it collides and the current one is not right on top of the one below - i.e. it can fall
                        if brick0.z0 != brick1.z1 + 1:
                            falls += 1
                            # update z-position
                            brick0.set_z(brick1.z1+1, brick1.z1+1 + brick0.z1-brick0.z0)  # noqa
                        brick0.landed = True
                        brick0.supported_by.add(brick1)
                        brick1.support.add(brick0)
                    else:
                        if brick0.z0 - brick1.z1 == 1:
                            brick0.supported_by.add(brick1)
                            brick1.support.add(brick0)
            if not brick0.landed:
                if brick0.z0 != 1:
                    falls += 1
                brick0.landed = True
                brick0.set_z(1, 1 + brick0.z1 - brick0.z0)

            bricks.sort(key=lambda b: b.z0)

    return falls


def parse():
    content = read_input(day=22, delimiter='\n')

    x_limit = 0
    y_limit = 0
    z_limit = 0

    bricks = []
    for i, line in enumerate(content):
        (x0, y0, z0), (x1, y1, z1) = [
            tuple(map(int, token.split(','))) for token in line.split('~')]

        x_limit = max(x_limit, x1)
        y_limit = max(y_limit, y1)
        z_limit = max(z_limit, z1)

        bricks.append(Brick(i, x0, y0, z0, x1, y1, z1))

    return bricks


def solve_part_one():
    bricks = parse()
    fall(bricks)

    # those brick that, alone, support other bricks, cannot be disintegrated.
    cannot_be_disintegrated = set(
        [b.supported_by.pop() for b in bricks if len(b.supported_by) == 1])

    ans = len(bricks) - len(cannot_be_disintegrated)
    print(f"part 1: {ans}")


def solve_part_two():
    bricks = parse()
    fall(bricks)

    ans = 0

    # remove a brick and see how many fall. Iterate thourgh all bricks and sum up all fallen bricks.
    # it is very inefficient..takes around 15 minutes.
    for i in range(len(bricks)):
        bricks_minus_one = [Brick(b.id, b.x0, b.y0, b.z0, b.x1, b.y1, b.z1) for b in bricks]  # noqa
        bricks_minus_one.pop(i)

        falls = fall(bricks_minus_one)
        ans += falls

    print(f"part 2: {ans}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
