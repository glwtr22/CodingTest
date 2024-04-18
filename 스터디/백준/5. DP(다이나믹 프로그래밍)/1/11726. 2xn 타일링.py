# n = int(input())
# dp = [0] * (n+2)  # (n+1) 하면 왜 런타임 에러가 나는지 ??
#
# dp[1] = 1
# dp[2] = 2
# for i in range(3, n+1):
#     dp[i] = dp[i - 2] + dp[i - 1]
#
# print(dp[n] % 10007)


n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])