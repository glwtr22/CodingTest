import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

init_numbers = list(map(int, input().split()))
for num in init_numbers:
    hq.heappush(heap, num)

for i in range(n-1):
    numbers = list(map(int, input().split()))
    for num in numbers:
        if heap[0] < num:
            hq.heappush(heap, num)
            hq.heappop(heap)

print(heap[0])