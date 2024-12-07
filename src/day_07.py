from utils import *
from itertools import *
from functools import *


def is_valid(target, current, rest):
    if not rest:
        return target == current
    value = rest.pop(0)
    new_current_plus = current + value
    new_current_mul = current * value
    return is_valid(target, new_current_plus, rest.copy()) or is_valid(
        target, new_current_mul, rest.copy()
    )


def part_01(example=False):
    lines = read_lines(day=7, example=example, part=1)

    test_values = [int(line.split(":")[0]) for line in lines]
    expressions = [
        [int(value) for value in line.split(":")[1].strip().split(" ")]
        for line in lines
    ]
    tmp = map(
        lambda target, values: target if is_valid(target, 0, values) else 0,
        test_values,
        expressions,
    )

    result = sum(tmp)

    print(f"result day 01 part 01: {result}")
    return result


def is_valid_dos(target, current, rest):
    if not rest:
        return target == current
    value = rest.pop(0)
    new_current_plus = current + value
    new_current_mul = current * value
    new_current_concat = int(str(current) + str(value))
    return (
        is_valid_dos(target, new_current_plus, rest.copy())
        or is_valid_dos(target, new_current_mul, rest.copy())
        or is_valid_dos(target, new_current_concat, rest.copy())
    )


def part_02(example=False):
    lines = read_lines(day=7, example=example, part=2)

    test_values = [int(line.split(":")[0]) for line in lines]
    expressions = [
        [int(value) for value in line.split(":")[1].strip().split(" ")]
        for line in lines
    ]

    tmp = list(
        map(
            lambda target, values: target if is_valid_dos(target, 0, values) else 0,
            test_values,
            expressions,
        )
    )

    result = sum(tmp)

    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 3749


def test_02():
    assert part_02(example=True) == 11387


def main():
    test_01()
    part_01()
    test_02()
    part_02()


if __name__ == "__main__":
    main()
