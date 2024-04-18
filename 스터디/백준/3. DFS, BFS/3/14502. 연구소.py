from collections import deque
import copy
n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    queue.append((nx, ny))

    global answer
    zero = 0

    for i in range(n):
        zero += tmp_graph[i].count(0)

    answer = max(answer, zero)


def makeWall(cnt):
    # 벽 3개가 세워지면 바이러스 퍼뜨리기
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0  # 벽을 다시 허무는 과정 (백 트래킹)
                # 결국 bfs 까지 도달을 해서 bfs가 끝나면 두번째 makeWall 함수가 종료되고
                # 그 다음 줄이 실행이 될 텐데, 그럼 왜 효율적인 탐색인지 . . . ???

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
makeWall(0)
print(answer)