class Student:
    def __init__(self, name):
        self.name = name

    # invoke attribute what isn't exist, compiler will try to invoke like this
    # __getattr__(self, 'score')
    def __getattr__(self, attr):
        if attr == 'score':
            return 100
        if attr == 'age':
            return lambda x: x
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student('Ken')
print(s.name)
print(s.score)
print(s.age(10))
print(s.abc)