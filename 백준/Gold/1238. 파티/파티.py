# 다익스트라 두 번 쓰는 풀이
import heapq
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])

ans = dijkstra(X)
ans[0] = 0
for i in range(1, N+1):
    if i != X:
        res = dijkstra(i)
        ans[i] += res[X]

print(max(ans))