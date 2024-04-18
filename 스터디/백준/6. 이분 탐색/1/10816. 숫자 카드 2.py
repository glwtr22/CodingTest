import sys
input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

count = {}

# 가지고 있는 카드를 딕셔너리에 카드를 key, 개수를 value로 저장
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in candidate:
    result = count.get(target)
    if result == None:
        print(0, end =' ')
    else:
        print(result, end = ' ')




# import sys
# input = sys.stdin.readline
#
# n = int(input())
# num = list(map(int, input().split()))
# m = int(input())
# find = list(map(int, input().split()))
#
# num.sort()
#
# def count(num, f, start, end):
#     cnt = 0
#     while start <= end:
#         mid = (start + end) // 2
#         if num[mid] == f:
#             cnt += 1
#             idx = mid + 1
#             if idx < n:
#                 while num[idx] == f:
#                     cnt += 1
#                     idx += 1
#                     if idx >= n:
#                         break
#             idx = mid - 1
#             if idx >= 0:
#                 while num[idx] == f:
#                     cnt += 1
#                     idx -= 1
#                     if idx <= 0:
#                         break
#
#             return cnt
#         elif num[mid] > f:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return 0
#
#
# for f in find:
#     print(count(num, f, 0, n-1), end=' ')