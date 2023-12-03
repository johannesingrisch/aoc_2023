"""
Advent of Code 2023: Day 3
"""

# import data
INPUT_TEST = "data/03_test.txt"
INPUT_FULL = "data/03.txt"

# test results
RES_1 = 4361
RES_2 = 467835


# Puzzle 1


def solve_1(fn=INPUT_TEST) -> int:
    """
    Solve Puzzle 1
    """
    grid = open(fn, encoding="utf-8").read().splitlines()

    rowmax = len(grid)
    colmax = len(grid[0])

    # get coordinates of all symbols
    symbols = []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if not (ch.isdigit() or ch == "."):
                symbols.append((r, c))

    # using a set to store the first coordinate of all relevant numbers
    digit_coords = set()
    for r, c in symbols:
        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if cr < 0 or cr > rowmax or cc < 0 or cc > colmax:
                    continue
                if not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc - 1].isdigit():
                    cc -= 1
                digit_coords.add((cr, cc))

    part_numbers = []

    for r, c in digit_coords:
        nstr = ""
        while c < len(grid[r]) and grid[r][c].isdigit():
            nstr += grid[r][c]
            c += 1
        part_numbers.append(int(nstr))

    return sum(part_numbers)


# Puzzle 2


def solve_2(fn=INPUT_TEST) -> int:
    """
    Solve Puzzle 1
    """
    grid = open(fn, encoding="utf-8").read().splitlines()

    rowmax = len(grid)
    colmax = len(grid[0])

    # get coordinates of all symbols
    my_sum = 0
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "*":
                continue

            coords = set()

            # using a set to store the first coordinate of all relevant numbers
            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if cr < 0 or cr > rowmax or cc < 0 or cc > colmax:
                        continue
                    if not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1

                    coords.add((cr, cc))

            if len(coords) != 2:
                continue

            part_numbers = []

            for rdigit, cdigit in coords:
                nstr = ""
                while cdigit < len(grid[rdigit]) and grid[rdigit][cdigit].isdigit():
                    nstr += grid[rdigit][cdigit]
                    cdigit += 1
                part_numbers.append(int(nstr))

            gear_ratio = part_numbers[0] * part_numbers[1]
            my_sum += gear_ratio
    return my_sum


if __name__ == "__main__":
    assert solve_1() == RES_1
    print(f"Solution part one: {solve_1(fn = INPUT_FULL)}")

    assert solve_2() == RES_2
    print(f"Solution part two: {solve_2(fn = INPUT_FULL)}")
