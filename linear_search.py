lil = [1,2,3,4,5,6]
def test_linear_search(input_list, value_to_search, expected):
    result = linear_search(input_list, value_to_search)
    if expected == result:
        return True
    else:
        return False


def linear_search(input_list, value_to_search):
    for i,value in enumerate(input_list):
        if value == value_to_search:
            return i 

#print(test_linear_search(lil, 3, 2))
#print(test_linear_search(lil, 3, 3))

## short Lambda function code from Twitter
long_str = lambda test: len(test) > 12
print(long_str("ThetPaingMyo103"))

## fibonacci 
def fib_seq(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        print("Work")
        return fib_seq(n-1) + fib_seq(n-2)

fib_seq(5)