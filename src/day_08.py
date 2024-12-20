from utils import *
from itertools import *
from functools import *


def dist(a, b):
    return tuple(a - b for a, b in zip(a, b))


def part_01(example=False):
    lines = read_lines(day=8, example=example, part=1)

    antennas_at = {x: [] for line in lines for x in line if x != "."}
    antinodes = set([])

    for i, line in enumerate(lines):
        for j, cell in enumerate(list(line)):
            match cell:
                case ".":
                    pass
                case x:
                    antennas_at[x].append((i, j))

    bounds = (len(lines), len(lines[0]))

    for key in antennas_at:
        for antenna_a, antenna_b in [
            (a, b) for a, b in product(antennas_at[key], repeat=2) if a != b
        ]:
            d = dist(antenna_a, antenna_b)
            antinode = (antenna_a[0] + d[0], antenna_a[1] + d[1])
            if 0 <= antinode[0] < bounds[0] and 0 <= antinode[1] < bounds[1]:
                antinodes.add(antinode)
    result = len(antinodes)

    print(f"result day 01 part 01: {result}")
    return result


def part_02(example=False):
    lines = read_lines(day=8, example=example, part=2)

    antennas_at = {x: [] for line in lines for x in line if x != "."}
    antinodes = set([])

    for i, line in enumerate(lines):
        for j, cell in enumerate(list(line)):
            match cell:
                case ".":
                    pass
                case x:
                    antennas_at[x].append((i, j))

    bounds = (len(lines), len(lines[0]))

    for key in antennas_at:
        for antenna_a, antenna_b in [
            (a, b) for a, b in product(antennas_at[key], repeat=2) if a != b
        ]:
            antinodes.add(antenna_a)
            d = dist(antenna_a, antenna_b)
            antinode = (antenna_a[0] + d[0], antenna_a[1] + d[1])
            while 0 <= antinode[0] < bounds[0] and 0 <= antinode[1] < bounds[1]:
                antinodes.add(antinode)
                antinode = (antinode[0] + d[0], antinode[1] + d[1])
    result = len(antinodes)

    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 14


def test_02():
    assert part_02(example=True) == 34


def main():
    test_01()
    part_01()
    test_02()
    part_02()


if __name__ == "__main__":
    main()
