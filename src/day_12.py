from utils import *
from itertools import *
from functools import *


def discover_region(plots_at, plot, grid, discoverd, regions, original):

    up = (plot[0] - 1, plot[1])
    down = (plot[0] + 1, plot[1])
    left = (plot[0], plot[1] - 1)
    right = (plot[0], plot[1] + 1)

    adjacent_plots = [up, down, left, right]
    for adj_plt in adjacent_plots:
        if (
            adj_plt not in discoverd
            and 0 <= adj_plt[0] < len(grid)
            and 0 <= adj_plt[1] < len(grid[0])
            and grid[plot[0]][plot[1]] == grid[adj_plt[0]][adj_plt[1]]
        ):
            discoverd.append(adj_plt)
            plots_at.remove(adj_plt)
            regions[original] = (regions[original][0] + 1, regions[original][1])

            discover_region(plots_at, adj_plt, grid, discoverd, regions, original)
        elif (
            not (0 <= adj_plt[0] < len(grid))
            or not (0 <= adj_plt[1] < len(grid[0]))
            or grid[plot[0]][plot[1]] != grid[adj_plt[0]][adj_plt[1]]
        ):
            regions[original] = (regions[original][0], regions[original][1] + 1)
    return plots_at, adj_plt, grid, discoverd, regions, original


def part_01(example=False):
    lines = read_lines(day=12, example=example, part=1)

    grid = []
    for line in lines:
        grid.append(list(line))

    plots_at = list(product(range(len(grid)), range(len(grid[0]))))

    discoverd = []
    regions = {}
    while plots_at != []:
        plot = plots_at.pop()
        discoverd.append(plot)
        regions[plot] = (1, 0)
        plots_at, plot, grid, discoverd, regions, original = discover_region(
            plots_at, plot, grid, discoverd, regions, plot
        )  # (size,external edges)

    print("\n".join("".join(line) for line in grid), "\n")

    print(regions)
    result = sum(ex_edges * size for size, ex_edges in regions.values())

    print(f"result day 01 part 01: {result}")
    return result


def part_02(example=False):
    lines = read_lines(day=12, example=example, part=2)

    result = -1

    print(f"day 01 part 2: {result}")
    return result


def test_01():
    assert part_01(example=True) == 1930


def test_02():
    assert part_02(example=True) == 1206


def main():
    test_01()
    part_01()
    # test_02()
    # part_02()


if __name__ == "__main__":
    main()
