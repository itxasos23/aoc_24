import os
import re
from dataclasses import dataclass
from pathlib import Path

EX_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
EX_INPUT_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

LOCAL_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = LOCAL_PATH.parent.absolute() / "inputs" / "day_03.txt"


@dataclass
class MulInstruction:
    position: int
    first: int
    second: int


@dataclass
class DoInstruction:
    position: int


@dataclass
class DontInstruction:
    position: int


class Day:
    def __init__(self):
        # self.input_str = EX_INPUT_2
        self.input_str = open(INPUT_PATH).read()

    def day_1(self):
        num = 0
        for instruction in self._get_instructions():
            if isinstance(instruction, MulInstruction):
                num += instruction.first * instruction.second
        return num

    def _parse_mul_instructions_part_1(self):
        part_1_regex = re.compile(r"mul\((?P<mul_1>\d+),(?P<mul_2>\d+)\)")
        matches = part_1_regex.finditer(self.input_str)

        return [(int(m[1]), int(m[2])) for m in matches]

    def day_2(self):
        enabled, num = True, 0
        for instruction in self._get_instructions():
            if isinstance(instruction, DoInstruction):
                enabled = True
            elif isinstance(instruction, DontInstruction):
                enabled = False
            elif isinstance(instruction, MulInstruction) and enabled:
                num += instruction.first * instruction.second
        return num

    def _get_instructions(self):
        instructions = []
        instructions.extend(
            [
                MulInstruction(m.start(), int(m.group(1)), int(m.group(2)))
                for m in self._get_mul_instructions()
            ]
        )
        instructions.extend(
            [DoInstruction(m.start()) for m in self._get_do_instructions()]
        )
        instructions.extend(
            [DontInstruction(m.start()) for m in self._get_dont_instructions()]
        )
        return sorted(instructions, key=lambda m: m.position)

    def _get_mul_instructions(self):
        mul_regex = re.compile(r"mul\((?P<mul_1>\d+),(?P<mul_2>\d+)\)")
        return mul_regex.finditer(self.input_str)

    def _get_do_instructions(self):
        do_regex = re.compile(r"do\(\)")
        return do_regex.finditer(self.input_str)

    def _get_dont_instructions(self):
        dont_regex = re.compile(r"don\'t\(\)")
        return dont_regex.finditer(self.input_str)


def day():
    print(f"Day 03: d1: {Day().day_1()}, d2: {Day().day_2()}")
