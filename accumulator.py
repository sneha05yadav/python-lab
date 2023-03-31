class MyAccumulator:
    def __init__(self):
        self.sum = 0
    def add(self, number): 
        self.sum += number
        return self.sum

A = MyAccumulator().add
print(A(10))     
print(A(20))      
print(A(-15))     
