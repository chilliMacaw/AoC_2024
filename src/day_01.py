from utils import *


def part_01(example=False):
    lines = read_lines(day=1, example=example, part=1)
    left = []
    right = []

    for line in lines:
        tmp = line.split("   ")
        left.append(int(tmp[0]))
        right.append(int(tmp[1]))

    left.sort()
    right.sort()
    result = sum(map(lambda l, r: abs(l - r), left, right))
    print(f"result day 01 part 01: {result}")
    return result


def part_02(example=False):
    lines = read_lines(day=1, example=example, part=2)
    left = []
    right = []

    for line in lines:
        tmp = line.split("   ")
        left.append(int(tmp[0]))
        right.append(int(tmp[1]))

    counter = {}

    for item in right:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    result = sum(map(lambda l: counter[l] * l if l in counter else 0, left))
    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 11


def test_02():
    assert part_02(example=True) == 31


def main():
    test_01()
    part_01()
    test_02()
    part_02()


if __name__ == "__main__":
    main()
