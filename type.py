# dynamic allocated class with type('class_name', (extends_class), {method and members})
class Hello(object):
    def hello(self, name='Micheal'):
        print('Hello, %s' % name)

h = Hello()
h.hello('Apple')

def fn(self, name='Micheal'):
    print('Hello, %s' % name)

Hello2 = type('Hello', (object,), dict(hello=fn))
h2 = Hello2()
h2.hello('Banana')

Hello3 = type('Hello', (object,), dict(hello=lambda s, n='Micheal': print('Hello, %s' % n)))
h3 = Hello3()
h3.hello()
