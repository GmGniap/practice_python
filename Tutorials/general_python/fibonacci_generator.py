def fibonacci(max):
    a,b = 0,1
    while a < max:
        yield a
        a,b = b, a+b
        
if __name__ == '__main__':
    fib_gen = fibonacci(100000)
    for fib_number in fib_gen:
        print(fib_number)