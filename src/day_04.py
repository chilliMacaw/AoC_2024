from utils import *
import re


def part_01(example=False):
    lines = read_lines(day=4, example=example, part=1)

    pattern = "XMAS"
    pattern_reverse = "SAMX"
    search_space = []

    amt_cols = len(lines[0])
    amt_lines = len(lines)

    # add all lines to search space
    for line in lines:
        search_space.append(line)

    # add all cols to search space
    for col in range(amt_cols):
        search_space.append("".join(line[col] for line in lines))

    # add diagonals to search space
    for col in range(amt_cols):
        search_space.append(
            "".join(
                lines[x][y]
                for x, y in range2d(
                    (0, col), (amt_lines, 0), lambda x, y: (x + 1, y - 1)
                )
            )
        )

    for line in range(1, amt_lines):
        search_space.append(
            "".join(
                lines[x][y]
                for x, y in range2d(
                    (line, amt_cols - 1),
                    (amt_lines - 1, 0),
                    lambda x, y: (x + 1, y - 1),
                )
            )
        )

    for col in (abs(i - (amt_cols - 1)) for i in range(amt_cols)):
        search_space.append(
            "".join(
                lines[x][y]
                for x, y in range2d(
                    (0, col), (amt_lines, amt_cols - 1), lambda x, y: (x + 1, y + 1)
                )
            )
        )

    for line in range(1, amt_lines):
        search_space.append(
            "".join(
                lines[x][y]
                for x, y in range2d(
                    (line, 0),
                    (amt_lines - 1, amt_cols - 1),
                    lambda x, y: (x + 1, y + 1),
                )
            )
        )

    matches = [re.findall(pattern, elem, flags=0) for elem in search_space]
    matches_reverse = [
        re.findall(pattern_reverse, elem, flags=0) for elem in search_space
    ]

    result = sum(map(lambda match: len(match), matches)) + sum(
        map(lambda match: len(match), matches_reverse)
    )

    print(f"result day 01 part 01: {result}")
    return result


def range2d(start, end, step_fn):
    x, y = start
    while x != end[0] and y != end[1]:
        yield (x, y)
        x, y = step_fn(x, y)
    yield (x, y)


def part_02(example=False):
    lines = read_lines(day=4, example=example, part=2)

    patterns = ["MAS", "SAM"]
    grid = []

    # find all the As and count the ones part of an  X-MAS

    for line in lines:
        grid.append(list(line))
    count = 0
    for line in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[line][col] == "A":
                diag_one = "".join(
                    [grid[line - 1][col - 1], grid[line][col], grid[line + 1][col + 1]]
                )
                diag_two = "".join(
                    [grid[line - 1][col + 1], grid[line][col], grid[line + 1][col - 1]]
                )
                if diag_one in patterns and diag_two in patterns:
                    count += 1

    result = count
    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 18


def test_02():
    assert part_02(example=True) == 9


def main():
    test_01()
    part_01()
    test_02()
    part_02()


if __name__ == "__main__":
    main()
