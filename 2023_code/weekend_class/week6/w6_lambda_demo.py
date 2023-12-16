## Normal Function


def add_values(x, y):
    return x + y


print(f"Normal : {add_values(5,10)}")

add_result = lambda x, y: x + y
print(f"Lambda : {add_result(5, 10)}")


## get first item of list
def get_first_item(lst):
    return lst[0]


first_val = lambda lst: lst[0]

print(f"Normal : {get_first_item([1,2,3])}")
print(f"Lambda : {first_val([1,2,3])}")

lst1 = [5, 2, 7, 4, 6, 8]

print(f"Lambda w/ sorted : {sorted(lst1, key= lambda x: x%2)}")
print(f"Lambda w/ Map : {list(map(lambda item: item**2, lst1))}")
print(f"Lambda w/ Filter : {list(filter(lambda num: num % 2 != 0, lst1))}")
