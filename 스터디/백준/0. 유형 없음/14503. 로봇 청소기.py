'''
로봇 청소기 작동 시작 후 작동 멈출 때까지
청소하는 칸의 개수
'''

import sys

input = sys.stdin.readline

graph = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

graph[r][c] = -1  # 현재 위치 청소 표시
count = 1  # 청소 칸수 카운팅
while graph[r][c] != 1:
    temp = False
    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3
        nr = r + dr[d]
        nc = c + dc[d]
        if graph[nr][nc] == 0:
            r = nr
            c = nc
            graph[r][c] = -1
            count += 1
            temp = True
            break

    if not temp:  # 현재 칸의 주변 4칸 중 청소할 칸이 없는 경우
        r += dr[d - 2]
        c += dc[d - 2]  # 후진

print(count)




# n, m = map(int, input().split())
# r, c, d = map(int, input().split())
#
# room = []
# room = [list(map(int, input().split())) for _ in range(m)]
# dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서
# ans = 0
# while True:
#     count = 0
#     if room[r][c] == 0:
#         room[r][c] = 2
#         ans += 1
#
#     for dx, dy in dd:
#         nx = r + dx
#         ny = c + dy
#         if 0 <= nx < m and 0 <= ny < n:
#             if room[nx][ny] == 0:
#                 count += 1
#     if count == 0:  # 4 방향에 청소할 칸 없는 경우 : 후진
#         dx, dy = dd[d]
#         r -= dx
#         c -= dy
#         if room[r][c] == 1:  # 후진 하려는 칸이 벽인 경우
#             break
#     else:  # 청소 할 칸이 하나라도 있는 경우
#         while True:
#             d = (d + 3) % 4  # 반시계 방향 90도 회전
#             dx, dy = dd[d]
#             r = r + dx
#             c = c + dy
#             if 0 <= r < m and 0 <= c < n:
#                 if room[r][c] == 0:
#                     room[r][c] = 2
#                     ans += 1
#                     break
#
# print(ans)