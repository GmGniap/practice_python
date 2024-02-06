## Nov 2 : Following Learning Python Design Patterns (2016) book

from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass
    
class Dog(Animal):
    def do_say(self):
        print("ဝုတ် ဝုတ်")

class Cat(Animal):
    def do_say(self):
        print("မြောင် မြောင်")
        
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()
    

## Client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Dog or Cat?")
    ff.make_sound(animal)