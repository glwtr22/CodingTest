# import sys
#
# N = int(input())
# travel_cost = [list(map(int, input().split())) for _ in range(N)]
# min_value = sys.maxsize
#
# def dfs_backtracking(start, next, value, visited):
#     global min_value
#
#     # 모든 도시 방문 후에
#     if len(visited) == N:
#         # 마지막 도시에서 출발 도시로 가는 비용이 0이 아닐 경우
#         if travel_cost[next][start] != 0:
#             min_value = min(min_value, value + travel_cost[next][start])
#         return
#
#     for i in range(N):
#         # 현재 도시에서 갈 수 있는 도시 and 이미 방문한 도시가 아님 and 비용값이 저장된 최솟값보다 작음
#         if travel_cost[next][i] != 0 and i not in visited and value < min_value:
#             visited.append(i)
#             dfs_backtracking(start, i, value + travel_cost[next][i], visited)
#             visited.pop()  # 방문을 완료했다면 방문 목록 해제
#
# for i in range(N):
#     dfs_backtracking(i, i, 0, [i])
#
# print(min_value)


import sys

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
visited = [0] * N

def backtrack(start, now, value, cnt):
    global ans
    if cnt == N:  # 원하는 깊이까지 도달 시
        if a[now][start]:
            value += a[now][start]
            ans = min(ans, value)
            return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            backtrack(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0


for i in range(N):
    visited[i] = 1
    backtrack(i, i, 0, 1)   # 처음 번호, 현재 번호, 합, 갯수
    visited[i] = 0

print(ans)


# 참고 풀이 1
# import sys
#
# def dfs(start, now, value, cnt):  # 처음 번호, 현재 번호, 합, 개수
#     global ans
#     if cnt == N:
#         if a[now][start]: # 마지막 탐색 노드에서 시작 노드로 가는 경로가 있으면
#             value += a[now][start]
#             if ans > value:
#                 ans = value
#         return
#
#     if value > ans:
#         return
#
#     for i in range(N):
#         if not visited[i] and a[now][i]:
#             visited[i] = 1
#             dfs(start, i, value + a[now][i], cnt + 1)
#             visited[i] = 0
#
#
# N = int(input())
# a = [list(map(int, input().split())) for _ in range(N)]
# ans = sys.maxsize
# visited = [0] * N
# for i in range(N):
#     visited[i] = 1
#     dfs(i, i, 0, 1)
#     visited[i] = 0


# def dfs(v, visited, cnt):
#     cost = 0
#     for i in range(n):
#         if i != v:
#             if visited[i] != 1:
#                 visited[i] = 1
#                 cost += graph[v][i]
#                 dfs(i, visited, cnt+1)
#
#
#
# # 시작 노드 전체 시도
# for i in range(n):
#     visited = [0 for _ in range(n)]
#     dfs(i, visited, 0)
