import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = -1
cnt = 0
def dfs(v, cnt):
    global result
    visited[v] = True
    if v == b:
        result = cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)

dfs(a, cnt)

print(result)