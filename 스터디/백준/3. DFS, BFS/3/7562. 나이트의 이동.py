# BFS

from collections import deque

t = int(input())

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(mat):
    q = deque()
    q.append((x, y))
    mat[x][y] = 1
    while q:
        a, b = q.popleft()
        if a == xx and b == yy:
            return mat[xx][yy] - 1
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if mat[nx][ny] == 0:
                    q.append((nx, ny))
                    mat[nx][ny] = mat[a][b] + 1


for _ in range(t):
    I = int(input())
    mat = [[0 for _ in range(I)] for _ in range(I)]
    x, y = map(int, input().split())
    xx, yy = map(int, input().split())
    result = bfs(mat)
    print(result)


# DFS : 시간 초과
# import sys
# sys.setrecursionlimit(10 ** 6)
#
# t = int(input())
#
# dx = [-2, -1, 1, 2, -2, -1, 1, 2]
# dy = [1, 2, 2, 1, -1, -2, -2, -1]
#
#
# def dfs(x, y, mat):
#     for ddx, ddy in zip(dx, dy):
#         nx = x + ddx
#         ny = y + ddy
#         if nx == xx and ny == yy:
#             if mat[nx][ny] == -1 or mat[nx][ny] > mat[x][y] + 1:
#                 mat[nx][ny] = mat[x][y] + 1
#                 break
#
#         if 0 <= nx < I and 0 <= ny < I:
#             if mat[nx][ny] == 0 or mat[nx][ny] > mat[x][y] + 1:
#                 mat[nx][ny] = mat[x][y] + 1
#                 dfs(nx, ny, mat)
#
#
# for _ in range(t):
#     I = int(input())
#     mat = [[0 for _ in range(I)] for _ in range(I)]
#     x, y = map(int, input().split())
#     xx, yy = map(int, input().split())
#     dfs(x, y, mat)
#     print(mat[xx][yy])
