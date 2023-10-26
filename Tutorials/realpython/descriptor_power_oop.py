## Using descriptor to be DRY

import math
class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected.")
        instance.__dict__[self._name] = value

class Circle:
    radius = PositiveNumber()
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return round(math.pi * self.radius**2, 2)

class Square:
    side = PositiveNumber()
    
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return round(self.side ** 2, 2)


circle = Circle(100)
print(circle.radius)

circle.radius = 0

square = Square(500)
print(square.side)
square.side = -10