S = input()
bomb = input()

stack = []
bombLen = len(bomb)

for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-bombLen:]) == bomb:
        for _ in range(bombLen):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')



# import sys

# S = sys.stdin.readline().rstrip()
# bomb = sys.stdin.readline().rstrip()

# import sys
# input = sys.stdin.readline
#
# line = input()
# bomb = input()
#
# l = len(bomb)    # 폭발 문자열의 길이
#
# idx = 1
# while idx != -1:
#     idx = line.find(bomb)
#     if idx != -1:
#         line = line[:idx] + line[idx + l:]
#
# if line == "":
#     print("FRULA")
# else:
#     print(line)
