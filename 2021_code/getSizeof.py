from sys import getsizeof

class Test:
    #print("Test Function")
    pass
a = 42
print("size of int", getsizeof(a))

a = True
print("size of boolean", getsizeof(a))

a = "Hello"
print("size of string", getsizeof(a))

a = Test()
print("size of object", getsizeof(a))