class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Name: %s' % self.name
    # usually same as __str__ -> so use assign to defined
    # def __repr__(self):
    #     return 'Name: %s' % self.name

    __repr__ = __str__

s = Student()
print(s) # -> executed with __str__
s # -> executed with __repr__