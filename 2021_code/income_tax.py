from typing import Type


monthly = input("Input your monthly salary.")
annual = int(monthly) * 12 

# print(f"Annual income - {annual}")
def check_parent() -> int:
    try:
        parent = int(input("Input 1 if you live with one of your parents OR input 2 if you live with Both. \n"))
        return cal_parent(parent)

    except Exception as e:
        print("Only Numbers 1 or 2 are allowed")
        check_parent()


def cal_parent(parent : int) -> int:
    try:
        if parent == 1:
            parent_val = 1000000
            return parent_val
        elif parent == 2:
            parent_val = 2 * 1000000
            return parent_val
        elif parent >= 3 or parent <= 0:
            raise ValueError("Input 1 or 2 only!")
    except ValueError as ve:
        print(type(ve), ve)
        check_parent()

def check_wife() -> str:
    try:
        wife = str(input("Input Y if you've wife OR input N if you don't"))
        return cal_wife(wife)
    
    except TypeError as te:
        print("Enter only Y or N")

def cal_wife(wife : str) -> int:
    try:
        if wife.upper() == 'Y':
            return 1000000
        else:
            return 0
    except Exception as e:
        print(type(e))
        check_wife()


if annual <= 12000000:
    print("You don't need to pay Tax")

else:
    p = check_parent()
    print(p)
    print(type(p))


    
