class Chain:
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, attr):
        if attr == 'users':
            return lambda x: Chain('%s/%s' % (self._path, 'users/%s' % x))
        return Chain('%s/%s' % (self._path, attr))

    def __str__(self):
        return self._path
    __repr__ = __str__


print(Chain().status.com.tw)
print(Chain().status.user.timeline.list)
print(Chain().users('micheal').repos)