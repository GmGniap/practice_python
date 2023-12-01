import re


def get_first_number(input_str):
    return re.search(r"(\d)", input_str)[1]


with open("./day1_input.txt", "r") as file:
    lines = file.readlines()
    total = sum(int(get_first_number(line) + get_first_number(line[::-1])) for line in lines)

print(total)
