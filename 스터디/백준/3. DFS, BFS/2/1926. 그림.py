import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
draw = []
for _ in range(n):
    draw.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global area
    area += 1
    draw[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if draw[nx][ny] == 1:
            dfs(nx, ny)

areas = []
for i in range(n):
    for j in range(m):
        if draw[i][j] == 1:
            area = 0
            dfs(i, j)
            areas.append(area)


print(len(areas))  # 갱신을 하는 방식으로 하면 더 메모리 효율적일 듯 ???
if len(areas) == 0:
    print(0)
    exit(0)
areas.sort()
max_area = areas.pop()
print(max_area)