n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = wine[0]
    elif i == 1:
        dp[1] = wine[0] + wine[1]
    else:
        # 마지막 잔을 마시지 않았을 때, 마지막 잔을 마시고 전 잔을 안 마셨을 때, 마지막 잔을 마시고 전 잔도 마셨을 때
        # 계단 오르기 문제와 유사한데, 마지막 잔을 꼭 마시지 않아도 되는 점만 다르다
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[n-1])


# 게단 오르기 문제랑 같이 보기