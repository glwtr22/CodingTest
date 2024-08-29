import sys, heapq
input = sys.stdin.readline

max_heap = []
n = int(input())
for i in range(n):
    num = int(input()) * -1
    if num == 0:
        print(heapq.heappop(max_heap) * -1 if max_heap else 0)
    else:
        heapq.heappush(max_heap, num)