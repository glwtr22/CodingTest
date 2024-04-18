import sys
sys.setrecursionlimit(10**6)

n = int(input())
draw = [[] for _ in range(n)]
draw_rg = [[] for _ in range(n)]

for i in range(n):
    row = input()
    for r in row:
        draw[i].append(r)
        draw_rg[i].append(r)

# draw_rg = draw의 문제점 ?!

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y, draw):
    col = draw[x][y]
    draw[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if draw[nx][ny] == col:
                dfs(nx, ny, draw)

def dfs_rg(x, y, draw_rg):
    col = draw_rg[x][y]
    draw_rg[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if col == 'R' or col == 'G':
                if draw_rg[nx][ny] == 'R' or draw_rg[nx][ny] == 'G':
                    dfs_rg(nx, ny, draw_rg)
            if col == 'B':
                if draw_rg[nx][ny] == 'B':
                    dfs_rg(nx, ny, draw_rg)

cnt = 0
for i in range(n):
    for j in range(n):
        if draw[i][j] != 0:
            dfs(i, j, draw)
            cnt += 1
print(cnt)

cnt2 = 0
for i in range(n):
    for j in range(n):
        if draw_rg[i][j] != 0:
            dfs_rg(i, j, draw_rg)
            cnt2 += 1
print(cnt2)