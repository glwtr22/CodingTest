#  BFS : 간선의 비용이 모두 같을 때, 최단 거리를 탐색하기 위해 사용할 수 있는 알고리즘

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 현재 위치에서 네 가지 방향으로 연결된 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물을 만난 경우
            if graph[nx][ny] == 0:
                continue
            # (0, 0) 위치로 돌아가지 못하게
            if nx == 0 and ny == 0:
                continue

            # 처음 방문하는 노드인 경우 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1     # 직전 노드의 최단 거리 값에 + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))