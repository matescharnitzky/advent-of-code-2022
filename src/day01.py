
from typing import List


# raw inputs
raw = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

# sparse inputs
examples = [int(x) if x != "" else "" for x in raw.split('\n')]


def calc_calories(items: List[int]) -> List[int]:

    calories = []
    calorie_counter = 0

    for item in items:
        if item != "":
            calorie_counter += item
        else:
            calories.append(calorie_counter)
            calorie_counter = 0

    return calories


def calc_top_n_calories(calories: List[int], n: int) -> int:

    sorted_calories = sorted(calories, reverse=True)

    return sum(sorted_calories[:n])


if __name__ == "__main__":
    # example
    calories = calc_calories(examples)
    print(f'Example #1 solution: {calc_top_n_calories(calories, 1)}')
    print(f'Example #2 solution: {calc_top_n_calories(calories, 3)}')

    # task
    with open("./data/day01.txt") as f:
        raw = f.read()
    inputs = [int(x) if x != "" else "" for x in raw.split('\n')]
    calories = calc_calories(inputs)
    print(f'Task #1 solution: {calc_top_n_calories(calories, 1)}')
    print(f'Task #2 solution: {calc_top_n_calories(calories, 3)}')
