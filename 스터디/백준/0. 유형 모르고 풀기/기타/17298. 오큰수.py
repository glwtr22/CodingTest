# 1. 인덱스만 스택에 넣는 풀이
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ans = [-1] * N
stack = [0]  # 인덱스 값 넣는 스택 : ans 변수에 값을 저장할 때 인덱스가 필요하기 때문에

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)


# 2. 숫자와 인덱스를 스택에 튜플로 넣어주는 풀이
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

ans = [-1] * N
stack = deque()

for i in range(N):
    while stack and stack[-1][0] < arr[i]:
        tmp, idx = stack.pop()
        ans[idx] = arr[i]
    stack.append((arr[i], i))

print(*ans)


# import heapq
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# for i in range(N):
#     tmp = arr[i + 1:]
#     heapq.heapify(tmp)
#
#     while True:
#         if len(tmp) == 0:
#             print('-1', end=' ')
#             break
#
#         NGE = heapq.heappop(tmp)
#         if NGE < arr[i]:
#             continue
#         if NGE > arr[i]:
#             print(NGE, end = ' ')
#             break



# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# for i in range(N):
#     for j in range(i + 1, N):
#         if arr[i] < arr[j]:
#             print(arr[j], end = ' ')
#             break
#     else:
#         print("-1", end = ' ')