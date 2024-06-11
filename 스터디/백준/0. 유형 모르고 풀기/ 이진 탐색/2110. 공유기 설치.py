import sys

input = sys.stdin.readline

n, c = map(int, input().split())
h = [int(input()) for i in range(n)]
h.sort()
start, end = 1, h[n-1] - h[0]
result = 0

if c == 2:
    print(h[n-1] - h[0])
else:
    while start < end:
        mid = (start + end) // 2

        count = 1
        ts = h[0]  # 마지막으로 설치된 공유기의 위치
        for i in range(n):
            if h[i] - ts >= mid:
                count += 1
                ts = h[i]

        if count >= c:
            result = mid
            start = mid + 1
        elif count < c:
            end = mid

    print(result)



# https://my-coding-notes.tistory.com/119



# import heapq
# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# n, c = map(int, input().split())
# house = []
# for _ in range(n):
#     house.append(int(input()))
#
# house.sort()
#
# com = combinations(house, c)
#
# max_min = 0
# for co in com:
#     wid = []
#     for i in range(c-1):
#         heapq.heappush(wid, co[i+1] - co[i])
#     max_min = max(max_min, heapq.heappop(wid))
#
# print(max_min)