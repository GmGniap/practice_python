### Learning Decorators from O'reilly

def deco(func):
    def inner():
        print("Running Inner")
    return inner

@deco
def target():
    print('Running Target')

def add(x,y):
    return x+y 

def apply(func ,x,y):
    return func(x,y)

print(apply(add,2,5))

