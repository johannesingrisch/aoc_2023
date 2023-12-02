# day one
"""
Advent of Code 2023
Day 1
"""

import re
import inflect

# import data
INPUT_TEST = "data/01_test.txt"
INPUT_FULL = "data/01.txt"
INPUT_TEST_2 = "data/01_test_2.txt"


# test results
RES_1 = 142
RES_2 = 281


# puzzle 1
def solve_1(fn: str = INPUT_TEST) -> int:
    """
    Solve puzzle 1
    """

    with open(fn, "r", encoding="utf-8") as f:
        calfile = [el for el in f.readlines()]

    my_sum = 0

    for el in calfile:
        matches = re.findall(r"\d", el)
        digit = int(matches[0] + matches[-1])
        my_sum += digit

    return my_sum


# puzzle 2
def solve_2(fn: str = INPUT_TEST_2) -> int:
    """
    Solve puzzle 2
    """
    with open(fn, "r", encoding="utf-8") as f:
        calfile = [el for el in f.readlines()]

    digits = list(range(1, 10))
    digits = list(range(0, 10))
    p = inflect.engine()
    p.number_to_words(digits[0])
    keys = [p.number_to_words(el) for el in digits]
    values = [str(el) for el in digits]
    word_to_number = dict(zip(keys + values, values + values))
    word_to_number.pop("zero")

    nums = list(word_to_number.keys())
    pattern = re.compile("|".join(map(re.escape, nums)))

    my_sum = 0

    for el in calfile:
        matches = []
        start = 0

        while start < len(el):
            match = pattern.search(el, start)
            if not match:
                break
            matches.append(match.group())
            start = match.start() + 1
        first = word_to_number[matches[0]]
        last = word_to_number[matches[-1]]

        digit = int(first + last)
        my_sum += digit

    return my_sum


if __name__ == "__main__":
    assert solve_1() == RES_1
    print(f"Solution part one: {solve_1(fn = INPUT_FULL)}")

    assert solve_2() == RES_2
    print(f"Solution part two: {solve_2(fn = INPUT_FULL)}")
