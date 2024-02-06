import csv


def demo_write():
    with open("./data/hello.txt", "x") as file:
        file.write("Hello Mahn Thuta\n")
        file.write("How are you?\n")


def demo_read():
    with open("./data/hello.txt", "r") as readFile:
        # print(readFile.readlines()[-1])
        print(readFile.read())


def demo_append():
    with open("./data/hello.txt", "a") as appendFile:
        appendFile.write("Have you finish your homework?\n")


"""
p1, p2, p3
'KP', 'SWT', 'WH'
demo.csv

စု ၊ တု ၊ ပြု - စိတ်ကူးမယဥ်ရန်။ 

API response -> JSON / csv / xml
"""


def demo_write_csv():
    with open("./data/demo.csv", "w") as csvFile:
        writeData = csv.DictWriter(csvFile, fieldnames=["p1", "p2", "p3"])
        writeData.writerow({"p1": "KP", "p2": "SWT", "p3": "WH"})


def demo_read_csv():
    with open("./data/demo.csv", "r") as csvFile:
        read_data = csv.reader(csvFile)
        print(type(read_data))
        for row in read_data:
            print(row)


demo_read_csv()
