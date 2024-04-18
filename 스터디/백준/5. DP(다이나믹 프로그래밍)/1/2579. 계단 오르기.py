n = int(input())
st = [0] * 301      # n+1 말고
for i in range(1, n + 1):
    st[i] = int(input())

dp = [0] * 301      # n+1 말고 (n이 하드 코딩하는 인덱스를 커버하지 않는 작은 수로 들어올 수 있음)
dp[1] = st[1]
dp[2] = st[1] + st[2]
dp[3] = max(st[1] + st[3], st[2] + st[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + st[i - 1] + st[i], dp[i - 2] + st[i])

print(dp[n])




'''
계단 3개를 연달아 밟을 수 없기 때문에,
구하려는 게단의 직전과 전전이 아닌
3번째 전과 2번째 전이 기준이 되어야 한다.

마지막 게단은 밟힌 계단이니까
1. 직전 계단을 밟고 올라왔다면
전전 계단은 밟지 않았어야 하고

 2. 전전 게단을 밟고 +2해서
 마지막 계단을 밟은 것이라면
(i-3)인 경우에 대해 마지막 계단의 점수 값만 더해주면 된다

1,2 중에서 더 큰 값을 dp에 저장 !

https://sungmin-joo.tistory.com/18
'''

# 한결님 코드

# import sys
#
# stairs = int(sys.stdin.readline().strip())
# scores = [0]
#
# for _ in range(stairs):
#     scores.append(int(sys.stdin.readline().strip()))
#
# dp = [[0 for _ in range(2)] for _ in range(stairs + 1)]
#
# for i in range(1, stairs + 1):
#     if i == 1:
#         dp[i][0] = scores[i]
#         dp[i][1] = scores[i]
#     elif i == 2:
#         dp[i][0] = scores[i]
#         dp[i][1] = scores[i] + scores[i - 1]
#     else:
#         dp[i][0] = max(dp[i - 2][0], dp[i - 2][1]) + scores[i]
#         dp[i][1] = dp[i - 1][0] + scores[i]
#
# print(max(dp[stairs]))