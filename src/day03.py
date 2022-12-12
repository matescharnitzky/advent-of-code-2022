
from typing import List
from dataclasses import dataclass
import string


raw = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


@dataclass
class Rucksack:
    items: str
    compartment1: str
    compartment2: str
    common: str
    priority: int

    @staticmethod
    def parse_rucksack(s):
        m = int(len(s)/2)
        compartment1 = s[:m]
        compartment2 = s[m:]
        common = set(compartment1).intersection(set(compartment2)).pop()

        if common.isupper():
            priority = string.ascii_uppercase.find(common) + 27
        else:
            priority = string.ascii_lowercase.find(common) + 1

        return Rucksack(s, compartment1, compartment2, common, priority)


def calc_total_priority1(rucksacks: List[Rucksack]) -> int:

    return sum([rucksack.priority for rucksack in rucksacks])


def calc_total_priority2(rucksacks: List[Rucksack]) -> int:

    priorities = []
    group = []

    for i, v in enumerate(rucksacks):

        group.append(v.items)
        if (i + 1) % 3 == 0:
            common = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()

            if common.isupper():
                priority = string.ascii_uppercase.find(common) + 27
            else:
                priority = string.ascii_lowercase.find(common) + 1

            priorities.append(priority)
            group = []

    return sum(priorities)


if __name__ == "__main__":
    # example
    rucksacks = [Rucksack.parse_rucksack(s) for s in raw.splitlines()]
    total1 = calc_total_priority1(rucksacks)
    total2 = calc_total_priority2(rucksacks)
    print(f"Example 1 solution: {total1}")
    print(f"Example 2 solution: {total2}")

    # task
    with open("./data/day03.txt") as f:
        raw = f.read()
    rucksacks = [Rucksack.parse_rucksack(s) for s in raw.splitlines()]
    total1 = calc_total_priority1(rucksacks)
    total2 = calc_total_priority2(rucksacks)
    print(f"Task 1 solution: {total1}")
    print(f"Task 2 solution: {total2}")
