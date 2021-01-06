# Ref 
# https://dabeaz-course.github.io/practical-python/Notes/05_Object_model/01_Dicts_revisited.html 

class Stock:
    def __init__(self, names, share, price):
        self.names = names
        self.share = share 
        self.price = price 

s = Stock('Goog', 100, 4900.5)
print(s.__dict__)