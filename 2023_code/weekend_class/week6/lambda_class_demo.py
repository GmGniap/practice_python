def find_sum(x, y):
    return x + y


test = [0, 1, 5, 7, 8]


def find_first_item(lst):
    return lst[0]


first_item = lambda lst: lst[0]

# print(f"Normal func : {find_first_item(test)}")
# print(f"Lambda : {first_item(test)}")

total = lambda x, y: x + y

# print(total(5, 3))

## no body will write like that
# print((lambda x, y: x + y)(5, 3))

test = [{"name": "Mg Mg", "home": "Home"}, {"name": "Ma Ma", "home": "Home"}]

# -sorted, map, reduce, filter + Lambda

## map - Apply function to every item in iterable
test = [9, 0, 1, 5, 7, 8]

print(f"Result : {list(map(lambda item: item +2, test))}")

print(f"Sorted : {sorted(test, key=lambda x : x % 2)}")

print(f"Filtered: {list(filter(lambda y : y % 2 == 0, test))}")

## Python supports Functional Programming style , 



