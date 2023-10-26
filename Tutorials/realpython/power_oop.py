class SampleClass:
    class_attr = 100
    
    def __init__(self, instance_attr) -> None:
        self.instance_attr = instance_attr
    
    def method(self):
        print(f"Class attr: {self.class_attr}")
        print(f"Instance attr: {self.instance_attr}")

# print(SampleClass.class_attr)
# print(SampleClass.__dict__)

# instance = SampleClass("Here's instance")
# print(instance.__dict__)

## Dynamic Class
class User:
    pass

jane = User()
jane.name = "Jane Paing"
jane.job = "Data Engineer"
print(jane.__dict__)