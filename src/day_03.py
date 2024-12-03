from utils import *
import re


def part_01(example=False):
    lines = read_lines(day=3, example=example, part=1)
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    instructions = re.findall(pattern, "".join(lines), flags=0)

    result = sum(
        int(x) * int(y)
        for [x, y] in (
            re.findall(r"\d{1,3}", instruction, flags=0) for instruction in instructions
        )
    )
    print(f"result day 01 part 01: {result}")
    return result


def part_02(example=False):
    lines = read_lines(day=3, example=example, part=2)
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    instructions = re.findall(pattern, "".join(lines), flags=0)
    result = 0
    block = False

    for instruction in instructions:
        match instruction:
            case "do()":
                block = False
            case "don't()":
                block = True
            case _:
                [x, y] = re.findall(r"\d{1,3}", instruction, flags=0)
                if not block:
                    result += int(x) * int(y)
    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 161


def test_02():
    assert part_02(example=True) == 48


def main():
    test_01()
    part_01()
    test_02()
    part_02()


if __name__ == "__main__":
    main()
