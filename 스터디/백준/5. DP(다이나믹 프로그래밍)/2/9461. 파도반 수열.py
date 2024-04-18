T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)
    for i in range(1, N+1):
        if i == 1 or i == 2 or i == 3:
            dp[i] = 1
        elif i == 4 or i == 5:
            dp[i] = 2
        elif i == 6:
            dp[i] = 3
        elif i == 7:
            dp[i] = 4
        elif i == 8:
            dp[i] = 5
        else:
            dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])