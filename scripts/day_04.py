"""
AoC 2023: Day 4
"""

import re


# import data
INPUT_TEST = "data/04_test.txt"
INPUT_FULL = "data/04.txt"

# test results
RES_1 = 13
RES_2 = 30


# Puzzle 1


def solve_1(fn=INPUT_TEST) -> int:
    """Solve puzzle 1"""
    data = open(fn, encoding="utf-8").read().splitlines()

    def clean_by_line(string):
        match = re.search(r":\s*(.*)", string)
        tmp = match.group(1).strip()
        tmp = tmp.split("|")
        my_list = [el.split() for el in tmp]
        return my_list

    cards = []
    for card in data:
        cards.append(clean_by_line(card))

    def calc_points(card):
        win, have = card
        common = len(set(win) & set(have))
        if common == 0:
            res = 0
        else:
            res = 2 ** (common - 1)
        return res

    return sum([calc_points(card) for card in cards])


# Puzzle 2


def solve_2(fn=INPUT_TEST) -> int:
    """Solve puzzle 2"""
    data = open(fn, encoding="utf-8").read().splitlines()

    def clean_by_line(string):
        match = re.search(r":\s*(.*)", string)
        tmp = match.group(1).strip()
        tmp = tmp.split("|")
        my_list = [el.split() for el in tmp]
        return my_list

    cards = []
    for card in data:
        cards.append(clean_by_line(card))

    def calc_matches(card):
        win, have = card
        return len(set(win) & set(have))

    card_count = [1] * len(cards)

    for idx, card in enumerate(cards):
        matches = calc_matches(card)

        upperbound = min(idx + 1 + matches, len(cards))
        card_count[idx + 1 : upperbound] = [
            x + (1 * card_count[idx]) for x in card_count[idx + 1 : upperbound]
        ]

    return sum(card_count)


if __name__ == "__main__":
    assert solve_1() == RES_1
    print(f"Solution part one: {solve_1(fn = INPUT_FULL)}")

    assert solve_2() == RES_2
    print(f"Solution part two: {solve_2(fn = INPUT_FULL)}")
