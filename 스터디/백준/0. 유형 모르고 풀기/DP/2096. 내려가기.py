import sys
input = sys.stdin.readline

n = int(input())
tmp = list(map(int,input().split()))
dp1 = tmp
dp2 = tmp

for _ in range(n-1):
    a, b, c = map(int,input().split())
    dp1 = [a + max(dp1[0], dp1[1]), b + max(dp1), c + max(dp1[1], dp1[2])]
    dp2 = [a + min(dp2[0], dp2[1]), b + min(dp2), c + min(dp2[1], dp2[2])]

print(max(dp1), min(dp2))















import sys
input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j], max_dp[j+1])
            min_tmp[j] = a + min(min_dp[j], min_dp[j+1])
        elif j == 1:
            max_tmp[j] = b + max(max_dp[j-1], max_dp[j], max_dp[j+1])
            min_tmp[j] = b + min(max_dp[j-1], max_dp[j], max_dp[j+1])
        else:
            max_tmp[j] = c + max(max_dp[j], max_dp[j-1])
            min_tmp[j] = c + min(min_dp[j], min_dp[j-1])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]


print(max(max_dp), min(min_dp))


'''
전형적인 DP 문제를 자꾸 백트래킹 문제라고 생각하는 경향이 있음
코드 :  https://kyun2da.github.io/2021/04/27/goDown/

메모이제이션 : 필요한 만큼의 값만 저장하면서 갱신해나가는 알고리즘
'''



# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# maxSum = 0
# minSum = int(1e9)
#
#
# def findMax(depth, idx):
#     global maxSum
#
#     if depth == N:
#         return maxSum
#
#     if idx == 0:
#         findMax(depth+1, arr[depth+1][idx], idx)
#
#
# num = max(arr[0])
# maxSum += num
# idx = arr[0].index(num)
# findMax(0, idx)
#
# print(maxSum, minSum)