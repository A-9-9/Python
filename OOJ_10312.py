import sys
def fn(nums, a, b, sum):
    for i in range(nums + 1):
        if a*i + (nums - i)*b == sum:
            return i, nums - i

n = int(sys.stdin.readline())
for i in range(n):
    nums, a, b, sum = list(map(int, sys.stdin.readline().split(',')))
    print("%d,%d" % fn(nums, a, b, sum))