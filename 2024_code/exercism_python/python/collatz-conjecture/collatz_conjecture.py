## Recursive solution , but doesn't work for Count
def steps_recursive(number):
    print(f">> {number}")
    if number == 1:
        return
    return steps(number / 2) if number % 2 == 0 else steps((3 * number) + 1)

def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    count = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = (3 * number) + 1
        count += 1
    return count

