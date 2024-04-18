t = int(input())
p = [[0 for _ in range(15)] for _ in range(15)]

# 0층의 각 호수 저장
for i in range(1, 15):
    p[0][i] = i

# 각 층의 1호 저장
for i in range(1, 15):
     p[i][1] = p[i-1][1]

for i in range(1, 15): # 층마다 올라가면서
    for j in range(1, 15): # 호수 채우기
        p[i][j] = p[i][j-1] + p[i-1][j]  # 현재 층의 현재 호수보다 하나 작은 호수 + 현재 호수의 밑층 더하기

for _ in range(t):
    k = int(input())
    n = int(input())
    print(p[k][n])