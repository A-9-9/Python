import sys

def optimal_benifit(target):
    price = [1, 5, 8, 9, 10, 12, 17, 20, 24, 25]
    for i in range(len(price)):
        t = i + 1
        max_sud = -1
        for j in range(t):
            n1 = j
            n2 = t - j
            if n1 == 0:
                max_sud = max(max_sud, price[n2 - 1])
            else:
                max_sud = max(max_sud, price[n2 - 1] + price[n1 - 1])
        price[i] = max_sud
    print(price)
    return price[target - 1]

def optimal_benifit2(target):
    price = [1, 5, 8, 9, 10, 12, 17, 20, 24, 25]
    for i in range(len(price)):
        t = i + 1
        max_sud = -1
        for j in range(t):
            n1 = j
            n2 = t - j

            max_sud = max(max_sud, price[n2 - 1] if n1 == 0 else price[n2 - 1] + price[n1 - 1])

        price[i] = max_sud
    print(price)
    return price[target - 1]



# length = int(sys.stdin.readline())
# print(optimal_benifit(length))
optimal_benifit2(1)
optimal_benifit(1)