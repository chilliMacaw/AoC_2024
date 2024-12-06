from utils import *
from itertools import *
from functools import *
from collections import *


def is_valid(update, rules):
    previous_pages = []
    for page in update:
        if page in rules and any(item in previous_pages for item in rules[page]):
            return False
        previous_pages.append(page)
    return True


def part_01(example=False):
    lines = read_lines(day=5, example=example, part=1)
    i = 1
    for k, line in enumerate(lines):
        if not line:
            i = k
            break
    rules = {}
    updates = []

    for line in lines[:i]:
        tmp = line.split("|")
        rule = (int(tmp[0]), int(tmp[1]))
        rules[rule[0]] = (
            [rule[1]] if not rule[0] in rules else rules[rule[0]] + [rule[1]]
        )

    for line in lines[i + 1 :]:
        updates.append([int(elem) for elem in line.split(",")])

    result = sum(
        update[int((len(update) - 1) / 2)]
        for update in updates
        if is_valid(update, rules)
    )

    print(f"result day 01 part 01: {result}")
    return result


def part_02(example=False):
    lines = read_lines(day=5, example=example, part=2)

    i = 0
    for k, line in enumerate(lines):
        if not line:
            i = k
            break

    rules = {}
    updates = []

    for line in lines[:i]:
        tmp = line.split("|")
        rule = (int(tmp[0]), int(tmp[1]))
        rules[rule[0]] = (
            [rule[1]] if not rule[0] in rules else rules[rule[0]] + [rule[1]]
        )

    for line in lines[i + 1 :]:
        updates.append([int(elem) for elem in line.split(",")])

    invalid_updates = list(filter(lambda update: not is_valid(update, rules), updates))
    edge_sets = [
        [
            [(vertex, dest) for dest in rules[vertex] if dest in update]
            for vertex in update
            if vertex in rules
        ]
        for update in invalid_updates
    ]

    for i in range(len(edge_sets)):
        edge_sets[i] = sum(edge_sets[i], [])
    counters = []

    for edges in edge_sets:
        counters.append(Counter(edge[1] for edge in edges))

    fixed = []
    for i, (update, edges, counter) in enumerate(
        zip(invalid_updates, edge_sets, counters)
    ):
        page_que = [vertex for vertex in update if not vertex in counter]
        fixed.append([])
        while page_que:
            page = page_que.pop(0)
            fixed[i].append(page)
            for vert, dest in edges.copy():
                if vert == page:
                    edges.remove((vert, dest))
                    counter[dest] -= 1
                    if counter[dest] == 0:
                        page_que.append(dest)

    result = sum(update[int((len(update) - 1) / 2)] for update in fixed)
    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 143


def test_02():
    assert part_02(example=True) == 123


def main():
    test_01()
    part_01()
    test_02()
    part_02()


if __name__ == "__main__":
    main()
