from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
treasureMap = [[] for _ in range(n)]
for i in range(n):
    row = input()
    for r in row:
        treasureMap[i].append(r)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    cnt = 0   # 이동한 거리 카운트

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if treasureMap[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    queue.append((nx, ny))
    return cnt - 1


cnt = 0
for i in range(n):
    for j in range(m):
        if treasureMap[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))

print(cnt)


# https://emhaki.tistory.com/entry/python%EB%B0%B1%EC%A4%80-2589%EB%B2%88-%EB%B3%B4%EB%AC%BC%EC%84%ACBFS