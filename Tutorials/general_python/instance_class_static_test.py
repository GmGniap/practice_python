## Another explanation - https://realpython.com/instance-class-and-static-methods-demystified/

class Pizza:
    def __init__(self, i):
        self.ingredients = i
    
    def __repr__(self):
        return f'Eat all of ({self.ingredients!r})'
    
    @staticmethod
    def default_piz():
        print("Default here!")

# print(Pizza(['cheese','meat']))
# print(Pizza(1))

class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_promo(self, ratio):
        return ratio * self.salary
    
emp1 = Employee("Thet","Pai", 500)
print(emp1.salary)
print(emp1.give_promo(5))

