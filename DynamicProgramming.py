# dp[n][k][i] -> n: day, k: trade time, i: have on hands
# base case
# dp[-1][k][0] = 0 -> day are not begin, so don't have profit.
# dp[-1][k][1] = Integer.MIN_VALUE -> not begin, so use minimum number to avoid this.
# dp[n][0][0] = 0 -> because can't trade for get profit.
# dp[n][0][1] = Integer.MIN_VALUE -> the situation is have stock and can't trade, needs to avoid this situation.

# here is the Status translate function
# dp[n][k][0] = max(dp[n - 1][k][0], dp[n - 1][k][1] + price[n])
# dp[n][k][1] = max(dp[n - 1][k][1], dp[n - 1][k - 1][0] - price[n])

# leetcode question
# 121 -> k = 1
# dp[n][1][0] = max(dp[n - 1][1][0], dp[n - 1][1][1] + price[n])
# dp[n][1][1] = max(dp[n - 1][1][1], dp[n - 1][0][0] - price[n]) -> dp[n - 1][0][0] = 0
#               max(dp[n - 1][1][1], -prices[n])

# if k == infinity:
    # k = k - 1
# dp[n][k][1] = max(dp[n - 1][k][1], dp[n - 1][k - 1][0] - price[n])
#             = max(dp[n - 1][k][1], dp[n - 1][k][0] - price[n])
#             = max(dp[n - 1][1], dp[n - 1][0] - price[n])

# k == infinity and cooldown:
# dp[n][k][0] = max(dp[n - 1][k][0], dp[n - 1][k][1] + price[n])
# dp[n][k][1] = max(dp[n - 1][k][1], dp[n - 2][k - 1][0] - price[n])


# dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + price[i])
# dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - price[i])
# dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + price[i])
# dp[i][1][1] = max(dp[i - 1][1][1], -price[i])