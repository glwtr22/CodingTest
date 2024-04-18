import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    num = list(map(int, input().split()))
    heap = []
    total = 0

    for n in num:
        heapq.heappush(heap, n)

    while True:
        if len(heap) == 1:
            break
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        s = a + b
        total += s
        heapq.heappush(heap, s)

    print(total)
