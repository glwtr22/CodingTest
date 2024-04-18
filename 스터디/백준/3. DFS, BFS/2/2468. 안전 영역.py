from collections import deque
import sys
input = sys.stdin.readline

# 입력 받고 저장
n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

safe = []  # 내리는 비의 양에 따라 생기는 안전 영역의 개수 저장 하는 리스트

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, mat, rain):
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0 and mat[nx][ny] > rain:
                queue.append((nx, ny))
                visited[nx][ny] = 1

for rain in range(0, 101):
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]  # bfs 돌 때 방문 여부 구분
    for i in range(n):
        for j in range(n):
            if mat[i][j] > rain and visited[i][j] == 0:  # 뒤에 조건 추가
                bfs(i, j, visited, mat, rain)
                cnt += 1
    safe.append(cnt)

safe.sort()
max_safe = safe.pop()
print(max_safe)



# from collections import deque
# import sys
# input = sys.stdin.readline
#
# # 입력 받고 저장
# n = int(input())
# mat = []
# for _ in range(n):
#     mat.append(list(map(int, input().split())))
#
# safe = []  # 내리는 비의 양에 따라 생기는 안전 영역의 개수 저장 하는 리스트
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     queue = deque([(x, y)])
#     visited[x][y] = 1
#     while queue:
#         a, b = queue.popleft()
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if visited[nx][ny] == 0:
#                 queue.append((nx, ny))
#
# for rain in range(0, 101):
#     cnt = 0
#     check = [[0 for _ in range(n)] for _ in range(n)]  # 잠긴 지점과 안잠긴 지점 구분
#     visited = [[0 for _ in range(n)] for _ in range(n)]  # bfs 돌 때 방문 여부 구분
#     for i in range(n):
#         for j in range(n):
#             if mat[i][j] <= rain:
#                 check[i][j] = 1  # 1이 잠김 표시
#
#     for i in range(n):
#         for j in range(n):
#             if check[i][j] == 0:
#                 bfs(i, j)
#                 cnt += 1
#     safe.append(cnt)
#
# safe.sort()
# max_safe = safe.pop()
# print(max_safe)