class Ten:
    def __get__(self, obj, objtype=None):
        return 10

class A:
    x = 5
    y = Ten()

import logging
logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:
    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info("Accessing %r giving %r", 'age', value)
        return value
    
    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        standard_age = 10
        if value < standard_age:
            logging.error("Age is being less than 10")
        obj._age = value

class Person:
    age = LoggedAgeAccess()
    
    def __init__(self, name, age) -> None:
        self.name = name    # Regular instance attr
        self.age = age      # Calls __set__()
    
    def birthday(self):
        self.age += 1       # calls both __get__() and __set__()

paing = Person('Paing', 20)
thet = Person('Thet', 50)

print(paing.__dict__)
print(paing.age)
print("---x---")
print(paing.birthday())