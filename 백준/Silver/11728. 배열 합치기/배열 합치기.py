import heapq
from collections import deque

n, m = map(int, input().split())
a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))

answer = []

while a:
    heapq.heappush(answer, a.popleft())
while b:
    heapq.heappush(answer, b.popleft())

for _ in range(len(answer)):
    print(heapq.heappop(answer), end=' ')

'''
정렬되어 있는 두 배열 a, b
두 배열을 합친 후, 정렬해서 출력하기
'''