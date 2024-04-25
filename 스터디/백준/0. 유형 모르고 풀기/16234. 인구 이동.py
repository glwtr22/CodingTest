from collections import deque

n, l, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(A[nx][ny] - A[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))

    return union


result = 0

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                if len(country) > 1:
                    flag = 1
                    people = sum(A[x][y] for x, y in country) // len(country)

                    for x, y in country:
                        A[x][y] = people


    if flag == 0:
        print(result)
        break

    result += 1


# https://yuna0125.tistory.com/176



# N, L, R = map(int, input().split())
# A = []
# for _ in range(N):
#     A.append(list(map(int, input().split())))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# open = []
# def check(x, y):
#     global total
#     global cnt
#
#     total += A[x][y]
#     cnt += 1
#     open.append((x, y))
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N:
#             if L <= abs(A[x][y] - A[nx][ny]) <= R:
#                 check(nx, ny)
#
#     return
#
# total = 0
# cnt = 0
#
# check(0, 0)