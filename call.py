# is it can be invoked -> s()
class Student:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        return 'My name is %s' % self.name

s = Student('Micheal')
print(s())
print(callable(Student('a')))
print(callable(max))
print(callable([1, 2]))
print(callable(None))
print(callable('str'))