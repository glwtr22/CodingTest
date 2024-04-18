N = int(input())

dp = [1] * N

lines = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x : x[0])

for i in range(N):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))

'''
전깃줄을 교차하지 않게 끊기
끊어야 하는 전깃줄 최소 개수

각 전깃줄의 교차점 개수 구해서, 교차점 개수 많은 것부터 제거

LIS(Longest Increasing Subsequence), 최장 증가 부분 수열 알고리즘
'''