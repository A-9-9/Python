import sys

def toList(n):
    li = []
    for i in range(n):
        li.append(list(map(lambda x: int(x), sys.stdin.readline().split())))
    return li

def find_error(a, b, c):
    for j in range(len(c)):
        for k in range(len(c[j])):
            sud = c[j][k]
            node = -10000
            for l in range(att[1]):
                if a[j][l] != 9999 and b[l][k] != 9999:
                    sud -= a[j][l] * b[l][k]
                elif a[j][l] != 0 and b[l][k] != 0:
                    node = min(a[j][l], b[l][k])
            if node != -10000:
                return int(sud / node)

n = sys.stdin.readline()
for i in range(int(n)):
    att = list(map(lambda x: int(x), sys.stdin.readline().split(',')))
    a = toList(att[0])
    b = toList(att[2])
    c = toList(att[0])

    print(find_error(a, b, c))
