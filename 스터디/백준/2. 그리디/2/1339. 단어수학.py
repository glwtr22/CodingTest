import sys
n = int(sys.stdin.readline())
str = [sys.stdin.readline().strip() for _ in range(n)]
words = {}

for s in str:
    x = len(s)-1  # 지수로 올라갈 값
    for i in s:
        if i in words:
            words[i] += 10**x
        else:
            words[i] = 10**x
        x -= 1

_words = sorted(words.values(), reverse=True) # 딕셔너리의 value 값을 기준으로 내림차순

result = 0
n = 9
for k in _words:
    result += k * n
    n -= 1

print(result)


# n = int(input())
# str = []
# for _ in range(n):
#     str.append(input())
#
# str.sort()
# print(str)
#
# d = dict()
# n = 9
# for i in range(len(str)):
#     if i != (len(str) - 1):
#         for idx, ch in enumerate(str[i]):
#             if len(str[i]) - idx >= len(str[i+1]) and ch not in d:
#                 d[ch] = n
#                 n -= 1
#
#             if len(str[i]) - idx < len(str[i+1]):
#                 break
#             if ch in d:
#                 continue
#     else:
#         for ch in str[i]:
#             if ch in d:
#                 continue
#             else:
#                 d[ch] = n
#                 n -= 1
#
# print(d)
