n = int(input())

# DP 테이블 초기화
d = [0] * 1001

# 보텀업 다이나믹 플밍
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 796796

print(d[n])