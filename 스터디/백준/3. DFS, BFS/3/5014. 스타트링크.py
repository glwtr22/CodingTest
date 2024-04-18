from collections import deque
import sys
input = sys.stdin.readline
# f : 건물 높이 , s : 강호 현재 위치 , g : 목표 위치, u : 위로 , d : 아래로
f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1)

def bfs(start, cnt):
    q = deque([start])
    visited[start] = 1
    while q:
        x = q.popleft()
        if x == g:
            return visited[g] - 1
        for i in (x + u, x - d):
            if 1 <= i <= f and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
    return "use the stairs"

print(bfs(s, 0))


# 참고한 풀이

# from collections import deque
# import sys
# input = sys.stdin.readline
#
# f, s, g, u, d = map(int, input().split())
# visited = [0] * (f+1)
# count = [0] * (f+1)
#
# def bfs(v):
#     q = deque([v])
#     visited[v] = 1
#     while q:
#         v = q.popleft()
#         if v == g:
#             return count[g]
#         for i in (v+u, v-d):
#             if 0 < i <= f and not visited[i]:
#                 visited[i] = 1
#                 count[i] = count[v] + 1
#                 q.append(i)
#
#     if count[g] == 0:
#         return "use the stairs"
#
#
# print(bfs(s))




# 처음 풀이 : 이상함 .. ㅋ

# from collections import deque
# import sys
# sys.setrecursionlimit(10**6)
# # f : 건물 높이 , s : 강호 현재 위치 , g : 목표 위치, u : 위로 , d : 아래로
# f, s, g, u, d = map(int, input().split())
#
# visited = [0] * (f+1)
#
# def bfs(start, cnt):
#     global result
#
#     if start == g:
#         result = max(result, cnt)
#
#     q = deque([start])
#     visited[start] = 1
#     while q:
#         x = q.popleft()
#         for i in (x+u, x-d):
#             if 1 <= i <= f and visited[i] == 0:
#                 visited[i] = 1
#                 q.append(i)
#                 bfs(i, cnt+1)
#
#
# result = 0
# bfs(s, 0)
# if result == 0:
#     print("use the stairs")
# else:
#     print(result)