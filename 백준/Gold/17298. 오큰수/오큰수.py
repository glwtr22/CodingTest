from collections import deque
import sys
input = sys.stdin.readline

n =int(input())
num = list(map(int, input().split()))

ans = [-1] * n
stack = deque()

for i in range(n):
    while stack and num[stack[-1]] < num[i]:
        ans[stack.pop()] = num[i]
    stack.append(i)

print(*ans)