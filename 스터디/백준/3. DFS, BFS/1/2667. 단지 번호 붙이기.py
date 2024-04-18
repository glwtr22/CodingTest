import sys
sys.setrecursionlimit(10**6)

n = int(input())
mat = [[] for _ in range(n)]
for i in range(n):
    row = input()
    for r in row:
        mat[i].append(int(r))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

def dfs(x, y):
    global cnt   # 개수 세는 변수 전역화
    mat[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if mat[nx][ny] == 1:
            cnt += 1
            dfs(nx, ny)
            mat[nx][ny] = 0


for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            cnt = 1  # dfs 한 번 끝나면 값 저장 후 초기화
            dfs(i, j)
            result.append(cnt)

l = len(result)
print(l)
result.sort()
for r in result:
    print(r)