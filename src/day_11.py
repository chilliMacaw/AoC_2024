from utils import *
from itertools import *
from functools import *


def is_even(num):
    return num % 2 == 0


def recursive_stones(stone, i, lookup, limit=25):
    if i == limit:
        return 1
    if (stone, i) in lookup:
        return lookup[(stone, i)]
    s = str(stone)
    l = len(s)

    if stone == 0:
        result = recursive_stones(1, i + 1, lookup, limit)
    elif is_even(l):
        result = recursive_stones(
            int(s[: l // 2]), i + 1, lookup, limit
        ) + recursive_stones(int(s[l // 2 :]), i + 1, lookup, limit)
    else:
        result = recursive_stones(stone * 2024, i + 1, lookup, limit)
    lookup[(stone, i)] = result
    return result


def part_01(example=False):
    lines = read_lines(day=11, example=example, part=1)
    lookup = {}
    stones = [int(x) for x in lines[0].split(" ")]
    result = sum(recursive_stones(stone, 0, lookup) for stone in stones)

    print(f"result day 01 part 01: {result}")
    return result


def part_02(example=False):
    lines = read_lines(day=11, example=example, part=2)
    lookup = {}
    stones = [int(x) for x in lines[0].split(" ")]
    result = sum(recursive_stones(stone, 0, lookup, 75) for stone in stones)

    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 55312


def test_02():
    assert part_02(example=True) == 11387


def main():
    test_01()
    part_01()
    # test_02()
    part_02()


if __name__ == "__main__":
    main()
