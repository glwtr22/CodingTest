import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N, M = int(input()), int(input())
parent = [i for i in range(N+1)]
for i in range(N):
    link = list(map(int, input().split()))
    for j in range(N):
        if link[j] == 1:
            union_parent(parent, i+1, j+1)

travel = list(map(int, input().split()))
start = parent[travel[0]]
for i in range(1, M):
    if parent[travel[i]] != start:
        print("NO")
        break
else:
    print("YES")


'''
집합연산을 활용해서 같은 집합에 속해 있는지로 빠르게 파악 가능했음 !
'''






# from collections import deque
#
# N = int(input())
# M = int(input())
#
# mat = []  # 연결 여부 행렬
#
# for i in range(N):
#     mat.append(list(map(int, input().split())))
#
# travel = list(map(int, input().split()))
#
# graph = [[] for _ in range(N+1)]  # 노드 별 연결 노드 저장
# for i in range(N):
#     for j in range(i+1, N):
#         if mat[i][j] == 1:
#             graph[i+1].append(j+1)
#             graph[j+1].append(i+1)
#
# # 저장된 그래프 정보로 탐색
# edges = 0
# for i in range(N):
#     edges += mat[i].count(1)
#
# '''
# dfs bfs 통해서 경로가 있는지 확인하고 있으면 1 반환
# 반환된 1을 전부 더해서 travel 리스트의 길이-1 이랑 같으면 여행 가능
# 작으면 여행 불가능
# '''
# def check(graph, i, visited):
#     queue = deque([travel[i]])
#     visited[travel[i]] = True
#     find = 0
#     while queue:
#         v = queue.popleft()
#         for k in graph[v]:
#             if not visited[k]:
#                 if k == travel[i+1]:
#                     find = 1
#                     break
#                 queue.append(k)
#                 visited[k] = True
#
#         if find == 1:
#             return 1
#     return 0
#
#
# # if edges//2 >= N-1:   # 모든 노드가 무조건 연결되어 있다 > 여행 계획 가능
# #     print("YES")
# # else:  # 여행 계획 확인해야 함
# count = 0
# for i in range(len(travel)-1):
#     visited = [False] * (N+1)
#     count += check(graph, i, visited)
#     # print(count)
#
# if count == len(travel) - 1:
#     print("YES")
# else:
#     print("NO")




'''
인접 행렬 형태로 그래프 연결 주어짐
여행 가능 여부를 출력

1 2 3
1 2 가능한지
2 3 가능한지
'''