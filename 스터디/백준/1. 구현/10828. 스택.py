# N = int(input())
import sys
input = sys.stdin.readline
N = int(input())

stack = []
for i in range(N):
    comm = list(input().split())
    if comm[0] == 'push':
        stack.append(comm[1])
    elif comm[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif comm[0] == 'size':
        print(len(stack))
    elif comm[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:  # top
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)