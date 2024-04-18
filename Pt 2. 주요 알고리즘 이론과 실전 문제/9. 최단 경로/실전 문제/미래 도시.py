INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]  # 노드의 개수 n * n 만큼 생성

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):   # 간선의 개수 m 번만큼 입력 받기
    a, b = map(int, input().split())
    # 입력 받음과 동시에 그래프 초기화
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]  # 최단 거리 = 최단 거리 + 최단 거리

if distance == INF:
    print(-1)
else:
    print(distance)