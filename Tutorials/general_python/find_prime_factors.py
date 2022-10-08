import math
def find_prime(n):
    while n % 2 == 0:
        print("First Step : 2")
        n = n/2
    
    # print(f"After first step : {n}")
    # print(int(math.sqrt(n)))
    for i in range(3,int(math.sqrt(n))+1,2):
        print(f"Running : {i}")
        while n % i == 0:
            print(f"Second step : {i}")
            n = n/i
    
    print(f"After 2nd step: {n}")
    if n > 2:
        print(f'Last Step : {n}')

if __name__ == "__main__":
    n = 315
    find_prime(n)