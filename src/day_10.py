from utils import *
from itertools import *
from functools import *


def score(grid, x, y, elevation):
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        return []
    node = grid[x][y]
    if node != elevation:
        return []
    if elevation == 9 == node:
        return [(x, y)]
    return (
        score(grid, x + 1, y, elevation + 1)
        + score(grid, x - 1, y, elevation + 1)
        + score(grid, x, y + 1, elevation + 1)
        + score(grid, x, y - 1, elevation + 1)
    )


def part_01(example=False):
    lines = read_lines(day=10, example=example, part=1)
    grid = []
    for line in lines:
        grid.append([int(x) for x in list(line)])
    trailheads_at = set([])

    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == 0:
                trailheads_at.add((i, j))

    result = sum(len(set(score(grid, x, y, 0))) for x, y in trailheads_at)

    print(f"result day 01 part 01: {result}")
    return result


def score_dos(grid, x, y, elevation):
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        return 0
    node = grid[x][y]
    if node != elevation:
        return 0
    if elevation == 9 == node:
        return 1
    return (
        score_dos(grid, x + 1, y, elevation + 1)
        + score_dos(grid, x - 1, y, elevation + 1)
        + score_dos(grid, x, y + 1, elevation + 1)
        + score_dos(grid, x, y - 1, elevation + 1)
    )


def part_02(example=False):
    lines = read_lines(day=10, example=example, part=2)
    grid = []
    for line in lines:
        grid.append([int(x) for x in list(line)])
    trailheads_at = set([])

    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == 0:
                trailheads_at.add((i, j))

    result = sum(score_dos(grid, x, y, 0) for x, y in trailheads_at)

    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 36


def test_02():
    assert part_02(example=True) == 81


def main():
    test_01()
    part_01()
    test_02()
    part_02()


if __name__ == "__main__":
    main()
