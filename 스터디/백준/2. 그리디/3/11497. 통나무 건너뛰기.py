for i in range(int(input())):
    n = int(input())
    timbers = sorted(list(map(int, input().split())))
    level = 0
    for i in range(2, n):
        level = max(level, timbers[i] - timbers[i-2])
    print(level)


# import sys
#
# input = sys.stdin.readline
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     answer = [0 for i in range(n)]
#     num = list(map(int, input().split()))
#     num.sort()
#     front = 0
#     back = n-1
#     tmp = 0
#     for i in range(n):
#         if tmp == 0:
#             answer[front] = num[i]
#             front += 1
#             tmp = 1
#         else:
#             answer[back] = num[i]
#             back -= 1
#             tmp = 0
#
#     sub = []
#     for i in range(n-1):
#         sub.append(abs(answer[i] - answer[i+1]))
#     print(max(sub))