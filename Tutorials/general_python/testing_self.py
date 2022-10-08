## Following tutorial - https://www.geeksforgeeks.org/self-in-python-class/

class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def show(self):
        print("Model is ", self.model)
        print("Color is ", self.color)

class Check:
    def __init__(self):
        print("This is constructor!")

obj = Check()
print(obj)

audi = Car("audi4", "yellow")
jeep = Car("Jeep22", "black")

audi.show()
jeep.show()
