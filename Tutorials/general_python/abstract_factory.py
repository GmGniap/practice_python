## Nov 2 : Following Learning Python Design Patterns (2016) book

from abc import ABCMeta, abstractmethod

class PizzaFactory(ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass
    
    @abstractmethod
    def createNonVegPizza(self):
        pass

class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()
    
    def createNonVegPizza(self):
        return ChickenPizza()
    
