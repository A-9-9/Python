import sys
def isPrime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isBothPrime(x, y):
    if abs(x - y) != 2:
        return False
    return isPrime(x) and isPrime(y)


n = int(sys.stdin.readline())
for i in range(n):
    x, y = list(map(int, sys.stdin.readline().split(',')))
    print("Y" if isBothPrime(x, y) else "N")
