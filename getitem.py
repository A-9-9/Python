# Use index or slice to get element from class
class Fib:
    def __getitem__(self, n):
        if isinstance(n, int):
            self.a, self.b = 1, 1
            for i in range(n):
                self.a, self.b = self.b, self.a + self.b
            return self.a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
                a, b = 1, 1
                L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L
print(Fib()[5])
print(Fib()[:5])