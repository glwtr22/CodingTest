# 도달 거리가 K인 도시 번호 전부 출력
# BFS로 돌면서 거리 K인 경우 전부 출력, 하나도 없으면 -1 출력

#1. 인자로 깊이 주면서 확인하는 풀이
from collections import deque
import sys

sys.setrecursionlimit(10**6)

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a)


city = []

def bfs(graph, v, visited, depth):
    q = deque([(v, 0)])
    visited[v] = True
    while q:
        n, depth = q.popleft()
        if depth == K:
            city.append(n)
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                q.append((i, depth+1))


bfs(graph, X, visited, 0)

if city:
    city.sort()
    for c in city:
        print(c)
else:
    print("-1")


# 2. distance 변수로 깊이 관리하는 풀이
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0  # 시작 노드는 최단 거리 0으로 초기화

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:  # 최소 거리가 갱신이 안 됐으면 (BFS 특성상 먼저 도달한 경우가 최단 거리 보장)
            distance[next_node] = distance[now] + 1 # 최소 거리 갱신
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)