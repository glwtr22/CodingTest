import heapq
import sys
INF = int(1e9)

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])

a, b = map(int, input().split())

dist = [INF] * (n+1)
prev_node = [0] * (n+1)    # 최단 경로 출력을 위한 변수

def dijkstra(a):
    q = []
    heapq.heappush(q, (0, a))
    dist[a] = 0
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for i in graph[now]:
            if dist[i[0]] > i[1] + cost:
                dist[i[0]] = i[1] + cost
                prev_node[i[0]] = now    # now -> i[0]
                heapq.heappush(q, (i[1] + cost, i[0]))

dijkstra(a)
print(dist[b])

path = [b]
now = b
while now != a:
    now = prev_node[now]
    path.append(now)
    
# now -> i[0] 순으로 경로가 이어질 때, prev_node[i[0]] = now 형태로 저장했기 때문에
# path에는 경로 역순으로 저장이 된다.
# 따라서, 경로를 뒤집어서 출력해주어야 한다.
path.reverse()

print(len(path))
print(' '.join(map(str, path)))