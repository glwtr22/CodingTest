import math

for tc in range(int(input())):
    x, y = map(int, input().split())
    dist = y - x
    sq = int(math.sqrt(dist))
    etc = dist - sq ** 2
    count = sq * 2 - 1
    if etc == 0:
        print(count)
    elif etc <= sq:
        print(count + 1)
    else:
        print(count + 2)


# https://honggom.tistory.com/15





# import sys
# sys.setrecursionlimit(10**6)
#
# def dfs(x, y, k):
#     global cnt
#     global ans
#
#     cnt += 1
#
#     if x + 1 == y and 1 in (k - 1, k, k + 1):
#         ans = min(ans, cnt+1)
#         return
#
#     if x >= y:
#         return
#
#     for i in (k - 1, k, k + 1):  # 0 1 2  x=1  / -1 0 1
#         if x + i < y:
#             dfs(x + i, y, i)
#
#
# T = int(input())
#
# for _ in range(T):
#     x, y = map(int, input().split())
#     cnt = 0
#     ans = sys.maxsize
#     dfs(x + 1, y, 1)
#     print(ans)