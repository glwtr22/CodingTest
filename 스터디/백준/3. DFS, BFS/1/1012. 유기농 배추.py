from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    mat[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if mat[nx][ny] == 1:  # 방문하지 않은 노드인 경우
                queue.append((nx,ny))
                mat[nx][ny] = 0  # 방문 처리

for i in range(t):
    m, n, k = map(int, input().split())  # 배추밭 가로 길이 : m, 세로 길이 : n
    mat = [[0 for _ in range(n)] for _ in range(m)]
    cnt = 0

    for j in range(k):
        x, y = map(int, input().split())
        mat[x][y] = 1

    for a in range(m):
        for b in range(n):
            if mat[a][b] == 1:
                bfs(a, b)
                cnt += 1

    print(cnt)

# from collections import deque
# t = int(input())
# for _ in range(t):
#     m, n, k = map(int, input().split())
#     graph = [[i for i in range(1, m+1)] for _ in range(1, n+1)]
#     visited = [False] * (n+1)
#     arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
#     for _ in range(k):
#         a, b = map(int, input().split())
#         arr[b][a] = 1  # 좌표를 반대로
#
#     cnt = 0
#     for row in range(1, n+1):
#         queue = deque([row])
#         visited[row] = True
#         if arr[row-1][0] == 0:
#             continue
#         while queue:
#             v = queue.popleft()
#             visited[v] = True
#             for i in graph[v]:
#                 if not visited[i]:
#                     queue.append(i)
#                     visited[i] = True
#                     if arr[row-1][i-1] != 1:
#                         break
#         cnt += 1
#     print(cnt)