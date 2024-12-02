from pathlib import Path
import os

ex_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

LOCAL_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = LOCAL_PATH.parent.absolute() / "inputs" / "day_02.txt"

input_str = open(INPUT_PATH).read()
# input_str = ex_input


def _parse_input(input_str):
    rows = []
    for row in input_str.strip().splitlines():
        if not row:
            continue

        rows.append([r for r in map(int, row.strip().split(" "))])

    return rows


def _is_any_level_safe_damped(level):
    for idx in range(len(level)):
        this_level = level[:idx] + level[idx+1:]
        if _is_level_safe(this_level):
            return True
    return False


def _is_level_safe(level_list):
    if level_list[0] < level_list[-1]:
        return is_level_safe_increasing(level_list)
    elif level_list[0] > level_list[-1]:
        return is_level_safe_decreasing(level_list)
    else:
        return False


def is_level_safe_increasing(level_list):
    first_item = level_list[0]
    for item in level_list[1:]:
        if not 1 <= (item - first_item) <= 3:
            return False
        first_item = item
    return True


def is_level_safe_decreasing(level_list):
    first_item = level_list[0]
    for item in level_list[1:]:
        if not 1 <= (first_item - item) <= 3:
            return False
        first_item = item
    return True


def day_01():
    levels = _parse_input(input_str)
    safe_levels = 0

    for idx, level in enumerate(levels):
        if _is_level_safe(level):
            safe_levels += 1
    return safe_levels


def day_02():
    levels = _parse_input(input_str)
    safe_levels = 0

    for level in levels:
        if _is_level_safe(level):
            safe_levels += 1

        elif _is_any_level_safe_damped(level):
            safe_levels += 1

    return safe_levels


def day():
    print(f"d1: {day_01()}, d2: {day_02()}")
