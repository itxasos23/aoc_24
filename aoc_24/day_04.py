import itertools
import os
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np

EX_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

DEBUG_INPUT = """
123
456
789
"""

LOCAL_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = LOCAL_PATH.parent.absolute() / "inputs" / "day_04.txt"


class Day:
    xmas_re = re.compile("XMAS")

    def __init__(self):
        # self.input_str = '\n'.join([r for r in EX_INPUT.splitlines() if r])
        self.input_str = "\n".join(
            [r for r in open(INPUT_PATH).read().splitlines() if r]
        )
        self.input_matrix = np.array([list(row) for row in self.input_str.splitlines()])
        self.size = self.input_matrix.shape[0]

    def day_1(self):
        count = 0
        for row in self._get_rows_to_check():
            count += len(self.xmas_re.findall(row))
        return count

    def _get_rows_to_check(self):
        yield from itertools.chain(
            self._generate_rows(),
            self._generate_columns(),
            self._generate_right_diagonals(),
            self._generate_left_diagonals(),
        )

    def _generate_rows(self):
        yield from itertools.chain(
            (
                "".join(self.input_matrix[idx])
                for idx in range(self.input_matrix.shape[0])
            ),
            (
                "".join(self.input_matrix[idx])[::-1]
                for idx in range(self.input_matrix.shape[0])
            ),
        )

    def _generate_columns(self):
        yield from itertools.chain(
            (
                "".join(self.input_matrix[:, idx])
                for idx in range(self.input_matrix.shape[0])
            ),
            (
                "".join(self.input_matrix[:, idx])[::-1]
                for idx in range(self.input_matrix.shape[0])
            ),
        )

    def _generate_right_diagonals(self):
        yield from itertools.chain(
            (
                "".join(self.input_matrix.diagonal(idx))
                for idx in range(
                    -self.input_matrix.shape[0] + 1, self.input_matrix.shape[0]
                )
            ),
            (
                "".join(self.input_matrix.diagonal(idx))[::-1]
                for idx in range(
                    -self.input_matrix.shape[0] + 1, self.input_matrix.shape[0]
                )
            ),
        )

    def _generate_left_diagonals(self):
        yield from itertools.chain(
            (
                "".join(np.flipud(self.input_matrix).diagonal(idx))
                for idx in range(
                    -self.input_matrix.shape[0] + 1, self.input_matrix.shape[0]
                )
            ),
            (
                "".join(np.flipud(self.input_matrix).diagonal(idx))[::-1]
                for idx in range(
                    -self.input_matrix.shape[0] + 1, self.input_matrix.shape[0]
                )
            ),
        )

    def day_2(self):
        count = 0
        for idx in range(1, self.size - 1):
            for idy in range(1, self.size - 1):
                if self.input_matrix[idx, idy] == "A":
                    matches = self._find_matches_in_position(idx, idy)
                    count += matches

        return count

    def _find_matches_in_position(self, idx, idy):
        # only x pattern, not +
        values = [
            self.input_matrix[idx - 1, idy - 1],
            self.input_matrix[idx - 1, idy + 1],
            self.input_matrix[idx + 1, idy + 1],
            self.input_matrix[idx + 1, idy - 1],
        ]
        if "".join(values) in ("MMSS", "SMMS", "SSMM", "MSSM"):
            return 1
        else:
            return 0


def day():
    print(f"Day 04: d1: {Day().day_1()}, d2: {Day().day_2()}")
