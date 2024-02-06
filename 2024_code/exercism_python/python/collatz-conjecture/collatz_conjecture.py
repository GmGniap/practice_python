def steps(number):
    print(f">> {number}")
    if number == 1:
        return
    return steps(number / 2) if number % 2 == 0 else steps((3 * number) + 1)

steps(12)
