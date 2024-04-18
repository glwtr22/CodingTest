n = int(input())
node = list(map(int, input().split()))
del_node = int(input())

def dfs(v):
    node[v] = -2
    for i in range(n):
        if v == node[i]:
            dfs(i)

dfs(del_node)

cnt = 0
for i in range(n):
    if node[i] != -2 and i not in node:  # i 노드가 지워지는 노드가 아니고 && 자식이 트리 안에 없으면 (리프 노드가 아니면) 카운팅
        cnt += 1

print(cnt)



# 삭제할 노드는 애초에 그래프 형성 때부터 넣지 않는 풀이 : https://he-ya.tistory.com/50

import sys
sys.setrecursionlimit(10**6)

n = int(input())
node = list(map(int, input().split()))
del_node = int(input())

graph = [[] for _ in range(n)]
visited = [False] * n

for idx, n in enumerate(node):
    if n == -1:
        continue
    graph[n].append(idx)
    graph[idx].append(n)

# 노드 제거 (del_node와 부모 노드의 연결 끊기)
parent = node[del_node]
if parent == -1:
    # 루트 노드와 연결된 서브 트리 전체 삭제
    node[del_node] = 0
else:  # 아래 방향으로만 저장이 되게 연결 상태 저장
    del graph[parent][graph[parent].index(del_node)]
    del graph[del_node][graph[del_node].index(parent)]

# print(graph)

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    if len(graph[v]) == 1 and graph[v][0] == node[v]:
        cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0
for idx, n in enumerate(node):
    if n == -1:
        if len(graph[idx]) == 0:
            continue
        dfs(graph, idx, visited)
print(cnt)