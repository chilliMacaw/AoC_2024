from utils import *
from itertools import *
from functools import *

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)


class Position:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


def move(position, direction, grid, turns):
    grid[position.x][position.y] = "X"
    next_pos = Position(position.x + direction[0], position.y + direction[1])
    while grid[next_pos.x][next_pos.y] == "#":
        direction = next(turns)
        next_pos.x = position.x + direction[0]
        next_pos.y = position.y + direction[1]
    return next_pos, direction


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return Position(i, j)


def part_01(example=False):
    lines = read_lines(day=6, example=example, part=1)

    grid = []

    for line in lines:
        grid.append(list(line))

    turns = cycle([UP, RIGHT, DOWN, LEFT])

    position = find_start(grid)
    direction = UP

    while (
        position.x != 0
        and position.y != 0
        and position.x != len(grid) - 1
        and position.y != len(grid[0]) - 1
    ):
        position, direction = move(position, direction, grid, turns)

    count = 1
    for line in grid:
        for elem in line:
            if elem == "X":
                count += 1

    result = count

    print(f"result day 01 part 01: {result}")
    return result


def part_02(example=False):
    lines = read_lines(day=6, example=example, part=2)

    result = -1
    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 41


def test_02():
    assert part_02(example=True) == 6


def main():
    test_01()
    part_01()
    test_02()
    part_02()


if __name__ == "__main__":
    main()
