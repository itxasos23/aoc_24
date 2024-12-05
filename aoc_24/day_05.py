import itertools
import os
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from icecream import ic

EX_INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

LOCAL_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = LOCAL_PATH.parent.absolute() / "inputs" / "day_05.txt"


class Day:
    def __init__(self):
        # self.rules, self.updates = self._parse_input(EX_INPUT)
        self.rules, self.updates = self._parse_input(open(INPUT_PATH).read())

    def _parse_input(self, input_str):
        rules_str, updates_str = input_str.split("\n\n")

        rules = []
        for rule_str in rules_str.splitlines():
            if not rule_str:
                continue
            left, right = rule_str.strip().split("|")
            rules.append((int(left), int(right)))

        updates = []
        for update_str in updates_str.splitlines():
            if not update_str:
                continue
            values = list(map(lambda x: int(x), update_str.strip().split(",")))
            updates.append(values)

        return rules, updates

    def day_1(self):
        result = 0

        for update in self.updates:
            for rule in self._get_rules_that_apply(update):
                if not update.index(rule[0]) < update.index(rule[1]):
                    break
            else:
                result += update[(len(update) - 1) // 2]

        return result

    def day_2(self):
        result = 0

        for update in self._get_updates_that_break_at_least_one_rule():
            broken_rules = self._get_rules_broken_by(update)
            fixed_update = self._fix_update(update, broken_rules)
            result += fixed_update[(len(fixed_update) - 1) // 2]

        return result

    def _get_rules_broken_by(self, update):
        return [
            r
            for r in self._get_rules_that_apply(update)
            if not update.index(r[0]) < update.index(r[1])
        ]

    def _get_updates_that_break_at_least_one_rule(self):
        return [u for u in self.updates if len(self._get_rules_broken_by(u)) > 0]

    def _get_rules_that_apply(self, update):
        return [r for r in self.rules if r[0] in update and r[1] in update]

    def _fix_update(self, update, broken_rules):
        original_update = update.copy()
        all_rules = self._get_rules_that_apply(update)

        while broken_rules:
            # we flip the first two numbers, then find how many rules we're breaking
            rule = broken_rules[0]
            pos_0, pos_1 = update.index(rule[0]), update.index(rule[1])
            update[pos_0], update[pos_1] = update[pos_1], update[pos_0]

            new_broken_rules = self._get_rules_broken_by(update)

            if len(new_broken_rules) >= len(broken_rules):
                ic("This change breaks more rules than before!")

            broken_rules = new_broken_rules

        return update


def day():
    print(f"Day 05: d1: {Day().day_1()}, d2: {Day().day_2()}")
