import sys
def fn(s1, s2):
    if s1 == "" or s2 == "":
        return "N"

    li = []
    for i in s1:
        if s2.find(i) != -1 and not li.__contains__(i):
            li.append(i)
    ret = ''.join(sorted(li))
    return "N" if len(li) == 0 else ret

n = int(sys.stdin.readline())
l = []
for i in range(n):
    s1 = sys.stdin.readline().strip('\n')
    s2 = sys.stdin.readline().strip('\n')
    print(fn(s1, s2))

