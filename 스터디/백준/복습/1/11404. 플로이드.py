import sys
input = sys.stdin.readline

INF = int(1e9)

# 노드 간선 개수 입력 받기
n = int(input())
m = int(input())

# 2차원 리스트로 그래프 표현
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선 정보로 그래프 업데이트
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])  # 노선이 하나가 아닐 수 있음

# 점화식 구현 (k는 거쳐가는 노드)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('0', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()