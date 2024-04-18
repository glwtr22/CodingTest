import sys
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x, y, xx, yy = map(int, input().split())
    for i in range(x, xx):
        for j in range(y, yy):
            graph[j][i] = 1  # 왜 인덱스를 바꾸는 거지 ?? 아

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#dfs로 풀어보기
def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 1  # 1은 방문
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 0:
            dfs(nx, ny)

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

print(len(result))
result.sort()
for r in result:   # print(*result)
    print(r, end=' ')
