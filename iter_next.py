# Let class active with for loop
class Fib:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000: # condition of break loop
            raise StopIteration()
        return self.a
f = Fib()
for i in f:
    print(i)