# 1:54 ~
from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

s, X, Y = map(int, input().split())

def bfs(q):
    newVirus = []
    while q:
        virus, x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] == 0:
                mat[nx][ny] = virus
                newVirus.append((mat[nx][ny], nx, ny))
    return newVirus

if s == 0:
    print(mat[X-1][Y-1])
    exit(0)

cnt = 0

queue = []
for i in range(n):
    for j in range(n):
        if mat[i][j] != 0:
            queue.append((mat[i][j], i, j))
queue.sort()
q = deque(queue)

while True:
    # cnt != 0인 경우, 즉 바이러스가 증식 가능할 경우에 아래 수행
    newVirus = bfs(q)
    cnt += 1
    if cnt == s:
        break
    newVirus.sort()
    q = deque(newVirus)

print(mat[X-1][Y-1])


'''
배운 점
[1]
collections 라이브러리의 deque는 그냥 단순 큐
heapq가 삽입하면 알아서 정렬해주는 큐
(왜 이걸 헷갈리냐?)

[2]
당연한 말이지만,
시간 고려해서 효율적인 코드를 짜야 한다
'''

'''
1. deque에 0이 아니면 다 넣기 (알아서 정렬)
2. popleft해서 상하좌우로 증식 시키기

위 두 과정을 s초가 지날 때까지 수행
(x, y) 위치의 바이러스 출력
'''


'''
1~k번까지의 바이러스 종류
번호가 낮은 종류 바이러스부터 먼저 증식
증식 과정에서 이미 어떤 칸에 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다
S초가 지난 후에 (x, y) 좌표에 존재하는 바이러스 종류를 출력
바이러스 존재하지 않는 경우 0 출력
'''