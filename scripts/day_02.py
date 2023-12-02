# Day 2

# import data
INPUT_TEST = "data/02_test.txt"
INPUT_FULL = "data/02.txt"

# test results
RES_1 = 8
RES_2 = 2286


def solve_1(fn: str = INPUT_TEST) -> int:
    # load data
    thresholds = {"green": 13, "red": 12, "blue": 14}
    # read game results as nested dictionary
    games = {}
    with open(fn, "r") as f:
        for line in f:
            game, res = line.rstrip().split(":")
            game = int(game.split(" ")[1])
            res = res.split(";")

            resdict = {idx + 1: res[idx] for idx in range(len(res))}

            for key, value in resdict.items():
                pairs = [pair.strip().split() for pair in value.split(",")]
                pairs_dict = {color: int(count) for count, color in pairs}
                resdict[key] = pairs_dict

            games[game] = resdict

    def is_possible(inner_dict):
        return all(value <= thresholds[color] for color, value in inner_dict.items())

    my_sum = 0
    for key, value in games.items():
        condition = [is_possible(el) for el in value.values()]
        if all(condition):
            my_sum += key

    return my_sum


# puzzle 2


def solve_2(fn: str = INPUT_TEST) -> int:
    # read data
    games = {}
    with open(fn, "r") as f:
        for line in f:
            game, res = line.rstrip().split(":")
            game = int(game.split(" ")[1])
            res = res.split(";")

            resdict = {idx + 1: res[idx] for idx in range(len(res))}

            for key, value in resdict.items():
                pairs = [pair.strip().split() for pair in value.split(",")]
                pairs_dict = {color: int(count) for count, color in pairs}
                resdict[key] = pairs_dict

            games[game] = resdict

    # define functions
    def fewest_possible(inner_dict, fewest):
        for color, _ in fewest.items():
            if color in inner_dict.keys():
                if fewest[color] < inner_dict[color]:
                    fewest[color] = inner_dict[color]
        return fewest

    def power_of_game(game):
        fewest = {"red": 0, "blue": 0, "green": 0}
        for _, inner_dict in game.items():
            fewest = fewest_possible(inner_dict, fewest)

        power = 1
        for value in fewest.values():
            power *= value
        return power

    # calculate sum of powers
    my_sum = 0
    for key, game in games.items():
        my_sum += power_of_game(game)

    return my_sum


if __name__ == "__main__":
    assert solve_1() == RES_1
    print(f"Solution part one: {solve_1(fn = INPUT_FULL)}")

    assert solve_2() == RES_2
    print(f"Solution part two: {solve_2(fn = INPUT_FULL)}")
