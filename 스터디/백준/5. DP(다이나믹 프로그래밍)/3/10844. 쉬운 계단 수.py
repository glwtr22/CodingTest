N = int(input())

dp = [[0] * 10 for _ in range(N)]

dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for n in range(1, N):
    dp[n][0] = dp[n-1][1]  # 끝자리가 1이어야 다음 자리가 0일 수 있음
    dp[n][9] = dp[n-1][8]

    for k in range(1, 9):
        dp[n][k] = dp[n-1][k+1] + dp[n-1][k-1]

print(sum(dp[N-1]) % 1000000000)



# https://velog.io/@minchoul2/%EB%B0%B1%EC%A4%80-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98-Python
'''

'''

# n = int(input())
# dp = [0] * (n+1)
#
# for i in range(1, n+1):
#     if i == 1:
#         dp[i] = 9
#     else:
#         dp[i] = dp[i-1]*2 - i + 1

# print(dp[n]%1000000000)