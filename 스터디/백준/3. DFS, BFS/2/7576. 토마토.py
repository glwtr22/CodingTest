# from collections import deque
#
# m, n = map(int, input().split())
# box = []
# for _ in range(n):
#     box.append(list(map(int, input().split())))
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# queue = deque([])
#
# answer = 0
# for i in range(n):
#     for j in range(m):
#         if box[i][j] == 1:
#             queue.append((i, j))
# def bfs():
#     while queue:
#         a, b = queue.popleft()
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if box[nx][ny] == -1 or box[nx][ny] == 1:
#                 continue
#             # 0으로 안익은 토마토를 만난 경우
#             queue.append((nx, ny))
#             box[nx][ny] = box[a][b] + 1
#
# # 시작 점만 넣어 주면 bfs 에서 카운팅
# bfs()
# for b in box:
#     for j in b:
#         if j == 0:
#             print(-1)
#             exit(0)
#     answer = max(answer, max(b))
# print(answer-1)




from collections import deque

m, n = map(int, input().split())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
queue = deque([])
def bfs(queue):
    global time
    tmp = len(queue)
    while queue:
        a, b = queue.popleft()
        tmp -= 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if box[nx][ny] == -1 or box[nx][ny] == 1:
                continue
            # 0으로 안익은 토마토를 만난 경우
            queue.append((nx, ny))
            box[nx][ny] = 1
        if tmp == 0:
            tmp = len(queue)
            if queue:
                time += 1

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:  #
            queue.append((i, j))
# 시작 점만 넣어 주면 bfs 에서 카운팅
bfs(queue)

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
print(time)