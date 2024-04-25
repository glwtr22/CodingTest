n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i % 2 == 1:
        dp[i] = 0
    elif i == 2:
        dp[i] = 3
    else:
        dp[i] = dp[i-2] * dp[2] + sum(dp[:i-2]) * 2 + 2

print(dp[n])