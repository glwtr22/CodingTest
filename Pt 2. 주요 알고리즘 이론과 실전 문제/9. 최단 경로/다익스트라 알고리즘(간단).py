import sys
input = sys.stdin.readline  # 데이터 입력이 많을 때, input()을 sys.std.readline 으로 치환하는 코드
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())  # 시작 노드

graph = [[] for i in range(n+1)]  # 노드 간의 관계를 보여주는 graph 배열
visited = [False] * (n+1)  # 예제에서는 흑백으로 처리한 부분을 배열로 처리
distance = [INF] * (n+1)   # 최단 거리 테이블

# 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a 노드에서 b 노드로 가는 비용이 c
    graph[a].append((b, c))  # graph 리스트에 튜플을 원소로 갖게 저장

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:      # start 노드와 연결된 간선 정보를 distance 배열에 저장
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()  # 방문하지 않은 노드 중에서 최단 거리가 짧은 노드의 인덱스 반환
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:  # 도달할 수 없는 노드에 대한 처리
        print("INFINITY")
    else:
        print(distance[i])