# 다익스트라 알고리즘의 간단 버전을 heapq를 활용해 개선한 버전

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # n : 노드 개수 ,  m : 간선 개수
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 튜플의 첫 번째 요소로 정렬되기 때문에 (거리, 노드) 순서로 저장
        # 현재 now 노드의 최단 거리로 저장된 값이 이미 최단 거리이면 (즉 해당 노드가 이미 처리된 상태이면)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))  # 더 짧은 경로로 갱신이 된 노드들은 우선순위 큐에 삽입

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])