import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

# print(graph)

# 현재 탐색하는 노드에서 다른 노드까지의 최소 거리를 저장
def bfs(i):
    q = deque()
    q.append((i, 0))
    distance[i] = 0

    while q:
        now, dis = q.popleft()
        for n in graph[now]:
            if distance[n[0]] > dis + n[1]:
                q.append((n[0], dis + n[1]))
                distance[n[0]] = dis + n[1]
    return


ans = 0
for i in range(1, n+1):
    distance = [INF for _ in range(n+1)]
    bfs(i)
    t = 0
    for j in range(1, n+1):
        if distance[j] <= m:
            t += item[j-1]

    ans = max(ans, t)


print(ans)
