import heapq
import sys

n, m = map(int, input().split())
num = [int(x) for x in sys.stdin.readline().split()]
heapq.heapify(num)

for _ in range(m):
    n1 = heapq.heappop(num)
    n2 = heapq.heappop(num)
    heapq.heappush(num, n1+n2)
    heapq.heappush(num, n1+n2)

print(sum(num))


# n, m = map(int, input().split())
# num = list(map(int, input().split()))
#
# while m != 0:
#     num.sort()
#
#     one = num[0]
#     del num[0]
#     two = num[0]
#     del num[0]
#
#     total = one + two
#     num.append(total)
#     num.append(total)
#     m -= 1
#
# print(sum(num))

