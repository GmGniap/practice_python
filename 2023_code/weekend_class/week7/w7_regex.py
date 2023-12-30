import re

def check_be(word: str) -> bool:
    return True if re.search("^[bB][eE]", word) else False

def append_file(result):
    with open("./output.txt", "a") as file:
        file.write(f"{result}\n")

def write_new_file(filename):
    return open(filename, "w")
        
def read_file_and_result(filename):
    write_new_file("output.txt")
    with open(filename, "r") as read_file:
        for line in read_file:
            result = str(check_be(line))
            append_file(result)

read_file_and_result("w7_test.txt")
