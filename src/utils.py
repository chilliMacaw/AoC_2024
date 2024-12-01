import os
import sys
from itertools import cycle


def read_lines(day, example=False, part=1, transformer=str):
    """
    Read puzzle input either example or actual

    Args:
        day: number of the current day
        example : bool if input to read is example or not
        part : either 1 or 2 for puzzle one or two

    """
    try:
        if example:
            filename = f"day_{day}_part_{part}_example.txt"
        else:
            filename = f"day_{day}_part_1.txt"
        with open(os.path.join("inputs", filename)) as input_file:
            return [transformer(line.strip()) for line in input_file]
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
