## Following [tutorial](https://thepythoncorner.com/posts/2016-11-22-iterators-generators-python/)

class fibonacci:
    def __init__(self, max=1000000):
        self.a, self.b = 0,1
        self.max = max
    
    def __iter__(self):
        return self 
    
    def next(self):
        if self.a > self.max:
            raise StopIteration
        
        value_to_be_returned = self.a
        
        self.a,self.b = self.b, self.a + self.b
        return value_to_be_returned
    
    def __next__(self):
        return self.next()
    
if __name__ == "__main__":
    MY_FIBONACCI_NUMBERS = fibonacci()
    for fibonacci_number in MY_FIBONACCI_NUMBERS:
        print(fibonacci_number)