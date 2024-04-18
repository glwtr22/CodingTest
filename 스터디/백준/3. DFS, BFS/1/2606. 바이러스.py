from collections import deque

n = int(input())
con = int(input())
graph = [[] for i in range(n+1)]
for _ in range(con):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 무방향 그래프, graph[a], graph[b]에 동시에 연결 정보를 저장해야 한다

visited = [False] * (n+1)

cnt = 0
queue = deque([1])
visited[1] = True

while queue:
    v = queue.popleft()
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True

print(cnt-1)