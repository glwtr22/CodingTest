# https://jie0025.tistory.com/199
import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 최단 거리가 아님
            continue
        for i in graph[now]:  # 최단 거리임 > 작업 수행
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


# 시간 초과 / 메모리 초과 ...
# import sys
# sys.setrecursionlimit(10**6)
#
# V, E = map(int, input().split())
#
# graph = [[] for _ in range(V+1)]
#
# st = int(input())
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
#
# INF = 10**6
#
# def dfs(st, v, visited):
#     global result
#     # 경로가 존재하지 않는 경우에는 ???
#     if st == v:
#         result = min(result, visited[st])
#         return
#
#     for t in graph[st]:
#         n, w = t
#         visited[n] = visited[st] + w
#         dfs(n, v, visited)
#
# for i in range(1, V+1):
#     result = INF
#     visited = [0] * (V+1)
#     if i == st:
#         print(0)
#     else:
#         dfs(st, i, visited)
#         if result == INF:
#             print('INF')
#         else:
#             print(result)