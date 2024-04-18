import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(1, 11):
    for com in combinations(range(0,10), i):
        # com = list(com)
        # com.sort(reverse=True)  # 감소하도록 내림차순 정렬
        num = sorted(list(com), reverse=True)
        nums.append(int("".join(map(str, num))))

nums.sort()

try:
    print(nums[n])
except:
    print(-1)


# https://ryu-e.tistory.com/59


# n = int(input())
#
# count = -1
# ans = -1
# for i in range(1000001):
#     num = str(i)
#     cnt = 0
#     for j in range(len(num)-1):
#         if num[j] <= num[j+1]:
#             continue
#         cnt += 1
#     if cnt == len(num)-1:
#         count += 1
#
#     if count == n:
#         ans = i
#         break
# else:
#     ans = -1
#
# print(ans)
