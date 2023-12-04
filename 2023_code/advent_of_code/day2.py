import re


class CustomError(Exception):
    pass


def parse_check_rgb(txt):
    std_rgb = {"red": 12, "green": 13, "blue": 14}
    for i in txt.split(","):
        digit, colour = re.search(r"^(\d+)\s([a-z]+)", i.strip()).group(1, 2)
        if std_rgb[colour] < int(digit):
            raise CustomError("Greater than std.")


def find_possible_index(data):
    game_index, game_sets = data.split(":", 1)
    try:
        for game_set in game_sets.split(";"):
            parse_check_rgb(game_set)
        return int(re.search(r"(\d+)", game_index)[1])
    except CustomError:
        # print(f"Don't count this index : {game_index}")
        return None


def main():
    with open("./day2_input.txt", "r") as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            result = find_possible_index(line)
            if result:
                total += result
        print(f"Total : {total}")


main()
