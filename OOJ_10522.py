import sys
def gcd(x, y):
    if x > y:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x

n = int(sys.stdin.readline())
for i in range(n):
    s = list(map(int, sys.stdin.readline().split(",")))
    ret = -1
    for k in range(len(s)):
        for l in range(len(s)):
            if k != l:
                ret = max(ret, gcd(s[k], s[l]))
    print(ret)

