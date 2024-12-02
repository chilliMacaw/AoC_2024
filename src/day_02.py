from utils import *


def part_01(example=False):
    lines = read_lines(day=2, example=example, part=1)

    reports = [[int(level) for level in report.split(" ")] for report in lines]

    result = sum(is_valid(report=report) for report in reports)
    print(f"result day 01 part 01: {result}")
    return result


def is_valid(report):
    return all(
        [report[i + 1] - report[i] in range(1, 4) for i in range(len(report) - 1)]
    ) or all([report[i] - report[i + 1] in range(1, 4) for i in range(len(report) - 1)])


def part_02(example=False):
    lines = read_lines(day=2, example=example, part=2)

    reports = [[int(level) for level in report.split(" ")] for report in lines]

    result = sum(is_valid_with_skip(report=report) for report in reports)
    print(f"day 01 part 2: {result}")
    return result


def is_valid_increasing(report, lo, hi):
    if hi - lo <= 1:
        return True
    return all([1 <= report[i + 1] - report[i] <= 3 for i in range(lo, hi - 1)])


def is_valid_decreasing(report, lo, hi):
    if len(report) == 1:
        return True
    return all([1 <= report[i] - report[i + 1] <= 3 for i in range(lo, hi - 1)])


def is_valid_with_skip(report):
    # this is not needed because if this is true then the same list with either first or last entry missing is true as well as is checked in for loop below

    for i in range(len(report)):
        new_report = report[:i] + report[i + 1 :]

        if is_valid_increasing(new_report, 0, len(new_report)) or is_valid_decreasing(
            new_report, 0, len(new_report)
        ):
            return True

    return False


def test_01():
    assert part_01(example=True) == 2


def test_02():
    assert part_02(example=True) == 4


def main():
    test_01()
    part_01()
    test_02()
    part_02()


if __name__ == "__main__":
    main()
