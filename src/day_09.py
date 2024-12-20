from utils import *
from itertools import *
from functools import *


def part_01(example=False):
    lines = read_lines(day=9, example=example, part=1)

    disk = []
    id = 0

    is_block = True
    for cell in list(lines[0]):
        if is_block:
            disk.append(list(repeat(id, int(cell))))
            id += 1
            is_block = False
        else:
            disk.append(list(repeat(None, int(cell))))
            is_block = True

    disk = sum(disk, [])

    i = 0
    j = len(disk) - 1
    sum_ = 0
    while i < j:
        if disk[i] is None:
            disk[i] = disk[j]
            disk[j] = None
            i += 1
            j -= 1
            while disk[j] is None:
                j -= 1
        else:
            i += 1

    result = sum(i * item for i, item in enumerate(disk) if item != None)

    print(f"result day 01 part 01: {result}")
    return result


def find_place(disk, block, until):
    if block[0] is None:
        return disk
    for i, cell in enumerate(disk):
        if i >= until:
            return disk
        if block[1] == 0:
            return disk
        if cell is None:
            is_valid_space = all(x is None for x in disk[i : i + block[1]])
            if is_valid_space:
                return (
                    disk[:i]
                    + [block[0]] * block[1]
                    + disk[i + block[1] : until - block[1]]
                    + [None] * block[1]
                    + disk[until:]
                )
    return disk


def part_02(example=False):
    lines = read_lines(day=9, example=example, part=2)

    disk = []
    disk_space = []
    id = 0

    is_block = True
    for cell in list(lines[0]):
        if is_block:
            disk_space.append((id, int(cell)))
            disk.append(list(repeat(id, int(cell))))
            id += 1
            is_block = False
        else:
            disk_space.append((None, int(cell)))
            disk.append(list(repeat(None, int(cell))))
            is_block = True

    disk = sum(disk, [])

    for i, block in reversed(list(enumerate(disk_space)).copy()):
        until = sum(x[1] for j, x in enumerate(disk_space) if j <= i)
        disk = find_place(disk, block, until)
    result = sum(i * item for i, item in enumerate(disk) if item != None)

    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 1928


def test_02():
    assert part_02(example=True) == 2858


def main():
    test_01()
    part_01()
    test_02()
    part_02()  # may take a min especially in WSL


if __name__ == "__main__":
    main()
