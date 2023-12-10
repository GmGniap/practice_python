## List of lists
test1 = [
    ## [name , age]
    ["mg mg", "Home", 20],
    ["ma ma", "School", 18],
    ["hla hla", "Hospital", 30],
]

## List of dictionaries
test2 = [
    {"name": "mg mg", "location": "hospital", "age": 20},
    {"name": "ma ma", "age": 18, "location": "hospital"},
    {"name": "hla hla", "location": "hospital", "age": 30},
]


for i in test2:
    ## print age
    print(i["age"])
