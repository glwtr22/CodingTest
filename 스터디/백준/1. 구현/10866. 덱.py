from collections import deque
import sys

N = int(sys.stdin.readline())
deque = deque()
for i in range(N):
    comm = sys.stdin.readline().split()
    len_deque = len(deque)
    if comm[0] == 'push_front':
        deque.appendleft(comm[1])
    elif comm[0] == 'push_back':
        deque.append(comm[1])
    elif comm[0] == 'pop_front':
        if len_deque == 0:
            print(-1)
        else:
            print(deque[0])
            deque.popleft()
    elif comm[0] == 'pop_back':
        if len_deque == 0:
            print(-1)
        else:
            print(deque.pop())
    elif comm[0] == 'size':
        print(len_deque)
    elif comm[0] == 'empty':
        if len_deque == 0:
            print(1)
        else:
            print(0)
    elif comm[0] == 'front':
        if len_deque == 0:
            print(-1)
        else:
            print(deque[0])
    else:
        if len_deque == 0:
            print(-1)
        else:
            print(deque[len_deque-1])