import re

num_letters = {
    "nine": 9,
    "eight": 8,
    "seven": 7,
    "six": 6,
    "five": 5,
    "four": 4,
    "three": 3,
    "two": 2,
    "one": 1,
}


def get_first_number_index(input_str: str) -> (int, int):
    ## find the first digit number by regex
    if search_digit := re.search(r"(\d)", input_str):
        ### get the first digit number from regext Match object
        found_digit = int(search_digit[1])
        ## Find index of found value
        found_digit_index = input_str.index(str(found_digit))
        ## Return (value , index)
        return (found_digit, found_digit_index)

    ## if no digit contain
    return (None, None)


def get_last_number_index(input_str: str) -> (int, int):
    ### reverse string to easily find the last number
    rev_str = input_str[::-1]
    ### get last number and its index
    last_digit, last_rev_index = get_first_number_index(rev_str)

    ## to get correct index, we need to minus rev_index from (total_length - 1)
    last_correct_index = len(input_str) - 1 - last_rev_index

    return (last_digit, last_correct_index)


## Function to extract digit from word


def get_first_number(input_str):
    if search_digit := re.search(r"(\d)", input_str):
        return search_digit[1]


def get_digit_from_word(input_str):
    ## Loop over num_letters dictionary
    for word, num in num_letters.items():
        if search_word := re.search(f"({word})", input_str):
            return num_letters[search_word[1]]
    return None


def replace_digit_words(input_str: str) -> str:
    for word, num in num_letters.items():
        if re.search(f"({word})", input_str):
            ## replace only first occurance word
            input_str = re.sub(word, str(num_letters[word]), input_str, count=1)
    return input_str


def convert_and_find_digits(input_str):
    converted_str = replace_digit_words(input_str)
    print(f"After convert : {converted_str}")
    print(get_first_number(converted_str))
    print(get_first_number(converted_str[::-1]))


def get_number_from_right_end(input_str: str):
    max_length = 5

    ## starting from right ended index of string
    if len(input_str) < 3:
        return None
    last_index = len(input_str) - 1
    search_str = input_str[-max_length:]

    replaced_str = replace_digit_words(search_str)

    if re.search("\d", replaced_str):
        ## return the last number as string from replaced_str.
        return re.findall("\d", replaced_str)[-1]

    ## if not replaced , recursive right_end_replace() with string (reducing one word from last index)
    return get_number_from_right_end(input_str[:last_index])


def get_number_from_left_end(input_str):
    max_length = 5

    ## starting from left
    if len(input_str) < 3:
        return None

    ## search string will be always max 5 words from start
    search_str = input_str[:max_length]

    # print(f"Search_str : {search_str}")
    replaced_str = replace_digit_words(search_str)

    # print(f"Replaced str : {replaced_str}")
    if re.search("\d", replaced_str):
        ## return the first number as string from replaced_str.
        return re.findall("\d", replaced_str)[0]

    ## if not replaced , recursive with string (reducing one word from first index)
    return get_number_from_left_end(input_str[1:])


# test = get_number_from_right_end("two1ninegg6oneg")
# print(test)
# test2 = get_number_from_left_end("two1ninegg6oneg")
# print(test2)


# print(get_first_number_index("two1nine"))
# print("----")
# print(convert_and_find_digits("two1nine"))


def main():
    with open("./day1_input.txt", "r") as file:
        lines = file.readlines()

        ## convert words to digits
        total = sum(
            int(get_number_from_left_end(line) + get_number_from_right_end(line)) for line in lines
        )
        print(total)


main()
