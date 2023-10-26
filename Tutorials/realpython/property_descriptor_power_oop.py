## Property & Descriptor-Based Attributes
## Link - https://omnivore.app/paing/python-classes-the-power-of-object-oriented-programming-real-pyt-18b691e1233

import math

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if (not isinstance(value, int | float)) or value <= 0:
            raise ValueError("positive number needed")
        self._radius = value
    

# c = Circle(5)
# print(c.radius)

# c.radius = 100

c2 = Circle(-100)
c2.radius = 10
print(c2.radius)