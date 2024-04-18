import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]

def dfs(x, w):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = w + b
            dfs(a, w + b)

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))

# import sys
# sys.setrecursionlimit(10**6)
#
# n = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
#
# parent = []
# for _ in range(n-1):
#     p, c, w = map(int, input().split())
#     graph[p].append((c, w))
#     graph[c].append((p, w))
#     parent.append(p)
#
# # print(graph)
# def dfs(v, diam):
#     global result
#     result = max(result, diam)
#     for i in graph[v]:
#         n, w = i
#         diam += w
#         dfs(n, diam)
#
# maxNums = []
# for i in range(n):
#     if i not in parent: # 말단 노드일 때, 순회 시작
#         diam = 0
#         result = 0
#         dfs(i, diam)
#         maxNums.append(result)
#
# print(maxNums)
# print(max(maxNums))


# n = int(input())
# graph = [[] for _ in range(n+1)]
#
# parent = []
# for _ in range(n-1):
#     p, c, w = map(int, input().split())
#     graph[p].append((c, w))
#     graph[c].append((p, w))
#     parent.append(p)
#
# print(parent)
#
#
# # print(graph)
# def dfs(v, diam, visited):
#     global result
#     visited[v] = True
#     result = max(result, diam)
#     maxW = 0
#     for i in graph[v]:
#         n, w = i
#         maxW = max(maxW, w)
#
#
# maxNums = []
# for i in range(1, n+1):
#     if i not in parent: # 말단 노드일 때, 순회 시작
#         print('말단노드:', i)
#         diam = 0
#         result = 0
#         visited = [False] * (n + 1)
#         dfs(i, diam, visited)
#         maxNums.append(result)
# print(maxNums)
# print(max(maxNums))