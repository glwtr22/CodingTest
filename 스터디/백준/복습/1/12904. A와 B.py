s = input()
t = input()

while True:
    tLen = len(t)
    sLen = len(s)

    if tLen <= sLen:
        break

    if t[tLen-1] == 'A':  # t[-1]
        t = t[:tLen-1]

    else:
        t = t[:tLen-1]
        # 문자열 뒤집기  >>  t[::-1]
        tmp = list(t)
        tmp.reverse()
        t = ''.join(tmp)

if t == s:
    print(1)
else:
    print(0)

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
# s = input()
# t = input()
#
# def calculate(s, t):
#     if len(s) < len(t):
#         for i in range(2):
#             if i == 0:
#                 s += 'A'
#                 calculate(s, t)
#
#             else:
#                 s_list = list(s)
#                 s_list.reverse()
#                 _s = ''.join(s_list)
#                 _s += 'B'
#                 calculate(_s, t)
#
#     elif len(s) == len(t):
#         if s == t:
#             print(1)
#             exit(0)
#
# calculate(s, t)
# print(0)