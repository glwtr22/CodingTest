n = int(input())
a = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(1, n):
    # dp 테이블 따로 안만들고 있는 리스트 활용해서 메모리 효율적이다
    a[i][0] = min(a[i-1][1], a[i-1][2]) + a[i][0]
    a[i][1] = min(a[i-1][0], a[i-1][2]) + a[i][1]
    a[i][2] = min(a[i-1][0], a[i-1][1]) + a[i][2]

print(min(a[n-1][0], a[n-1][1], a[n-1][2]))








# N = int(input())
# cost = []
#
# for i in range(N):
#     cost.append(list(map(int, input().split())))
#
#
# for i in range(3):
#     dp = [0] * (N+1)
#     dp[0] = cost[0][i]
#     tmp = i
#     for j in range(1, N+1):
#         if tmp == 0:
#             idx1, idx2 = 1, 2
#         elif tmp == 1:
#             idx1, idx2 = 0, 2
#         else:
#             idx1, idx2 = 0, 1
#
#         cost1 = dp[j-1] + cost[j-1][idx1]
#         cost2 = dp[j-1] + cost[j-1][idx2]
#         if cost1 <= cost2:
#             dp[j] = dp[j-1] + cost[j-1][idx1]
#             tmp = idx1
#         else:
#             dp[j] = dp[j-1] + cost[j-1][idx2]
#             tmp = idx2
#     minCost = min(dp[N], 10**6+1)
#
# print(minCost)