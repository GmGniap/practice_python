def normal_write():
    newFile = open("Test.txt", "w")
    newFile.write("Hello World \n")
    newFile.write("File testing \n")
    newFile.close()


def normal_read():
    read_file = open("Test.txt", "r")
    # print(read_file.read())
    print(read_file.readline())
    print(read_file.readline())
    read_file.close()


def read_w_loop():
    read_file = open("Test.txt", "r")
    for line in read_file:
        # print(read_file.readline())
        print(line)
    read_file.close()


def normal_append():
    addFile = open("Test.txt", "a")
    addFile.write("New line appended!\n")
    addFile.close()


def write_w_with():
    with open("Test2.txt", "w") as file:
        file.write("Hello Weekend \n")
        file.write("File w/ with testing \n")
        file.write("မင်္ဂလာပါ\n")


## partial read first 2 characters
def read_partial():
    with open("Test2.txt", "r") as readFile:
        print(readFile.read(2))


import csv


def read_csv_file():
    with open("organizations-100.csv") as csvFile:
        csv_reader = csv.reader(csvFile)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names : {"| ".join(row)}')
            elif line_count == 2:
                print(f"{row[2]}")
            line_count += 1
        print(f"Total row count : {line_count}")


def write_csv_file():
    with open("test_csv.csv", mode="w") as csvFile:
        csv_writer = csv.writer(csvFile)
        csv_writer.writerow(["Name", "School", "Town"])
        csv_writer.writerow(["Ko Paing", "BEHS-2", "Monywa"])


# normal_write()
# normal_read()
# normal_append()
# read_w_loop()

## with WITH clause
# write_w_with()
# read_partial()

## Work w/ CSV
# read_csv_file()
write_csv_file()
