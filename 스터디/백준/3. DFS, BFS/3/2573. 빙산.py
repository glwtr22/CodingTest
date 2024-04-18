import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:  # 상하좌우 중 바다이면
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:  # 방문하지 않은 빙산이면
                    q.append((nx, ny))                     # 탐색
                    visited[nx][ny] = 1                     # 방문 처리

        if sea > 0:         # 한 빙산에 대해 상하좌우 모두 탐색했는데, 바다가 하나라도 있으면, seaList에 좌표값과 바다 개수 튜플로 저장
            seaList.append((x, y, sea))

    for x, y, sea in seaList:  # 빙산 녹이기
        graph[x][y] = max(0, graph[x][y] - sea) # max 함수로 음수가 되면 0으로 (분기 X)

    return 1  # 빙산 그룹 수 카운팅을 위해, 하나의 그룹을 탐색했다는 의미로 1을 리턴

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]: # 바다가 아니면
            ice.append((i, j))  # 빙산이 존재하는 위치 좌표만 ice에 저장

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice:  # 빙산이 존재하는 동안
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:  # 각각의 빙산에 대해서
        if graph[i][j] and not visited[i][j]:  # 방문하지 않은 빙산인 경우
            group += bfs(i, j)  # 탐색 시작
        if graph[i][j] == 0:   # 탐색이 끝나고, 해당 빙산이 바다가 되었으면, 제거 리스트에 저장
            delList.append((i, j))
    if group > 1:
        print(year)
        break

    ice = sorted(list(set(ice)-set(delList)))  # 바다가 된 빙산은 탐색하지 않아도 됨으로 ice 에서 제거
    year += 1

# 빙산이 전부 녹을 때까지 분리되지 않은 경우
if group < 2:
    print(0)



#
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# ice = [[] for _ in range(n)]
# for i in range(n):
#     row = list(map(int, input().split()))
#     for r in row:
#         ice[i].append([r, 0])
#
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
#
# def countSea(ice):
#     for i in range(n):
#         for j in range(m):
#             if ice[i][j][0] != 0:
#                 count = 0
#                 for k in range(4):
#                     nx = i + dx[k]
#                     ny = j + dy[k]
#                     if 0 <= nx < n and 0 <= ny < m and ice[nx][ny][0] == 0:
#                         count += 1
#                 ice[i][j][1] = count
#             else: # 바다인 경우 0 > 방문 여부용으로 활용  : 방문 시 -1
#                 ice[i][j][1] = 0
#
#
# def time(ice):
#     for i in range(n):
#         for j in range(m):
#             if ice[i][j][0] != 0:
#                 tmp = ice[i][j][0] - ice[i][j][1]
#                 if tmp <= 0:
#                     ice[i][j][0] = 0
#                     ice[i][j][1] = 0
#                 else:
#                     ice[i][j][0] = tmp
#     countSea(ice)
#
# def bfs(i, j, ice):
#     q = deque([(i, j)])
#     ice[i][j][1] = -1
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < m and ice[nx][ny][0] == 0:
#                 q.append((nx, ny))
#                 ice[nx][ny][1] = -1
#
#
# cntTime = 0
# while True:
#     time(ice) # 초기에는 island 1, time 내부 마지막 줄 countSea
#     cntTime += 1
#     island = 0
#     for i in range(n):
#         for j in range(m):
#             if ice[i][j][0] != 0:
#                 bfs(i, j, ice)
#                 island += 1
#     if island == 2:
#         break
#
# print(cntTime)