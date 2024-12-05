import os
from pathlib import Path

from icecream import ic

ex_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

LOCAL_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = LOCAL_PATH.parent.absolute() / "inputs" / "day_01.txt"

input_str = open(INPUT_PATH).read()
# input_str = ex_input


def _parse_input(input_str):
    left, right = [], []
    for row in input_str.splitlines():
        if not row:
            continue

        ln, rn = map(int, row.split("   "))
        left.append(ln)
        right.append(rn)

    return left, right


def _build_occurrence_dict(_list):
    occurence_dict = {}
    for item in _list:
        occurence_dict[item] = occurence_dict.get(item, 0) + 1

    return occurence_dict


def day_01():
    left, right = _parse_input(input_str)

    total_dif = 0
    for ln, rn in zip(sorted(left), sorted(right)):
        dif = abs(ln - rn)
        total_dif += dif

    return total_dif


def day_02():
    left, right = _parse_input(input_str)
    left_od = _build_occurrence_dict(left)
    right_od = _build_occurrence_dict(right)

    similarity = 0
    for k, v in left_od.items():
        similarity += k * v * right_od.get(k, 0)

    return similarity


def day():
    print(f"d1: {day_01()}, d2: {day_02()}")
