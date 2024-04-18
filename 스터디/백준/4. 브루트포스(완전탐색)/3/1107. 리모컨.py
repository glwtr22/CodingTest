import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

min_count = abs(100-target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        elif j == len(nums) - 1: # 고장 난 숫자 없이 마지막 자리수까지 온 경우에 업데이트
            min_count = min(min_count, abs(int(nums) - target) + len(nums))


print(min_count)




# n = int(input())
# m = int(input())
# butt = list(map(int, input().split()))
# norm = [i for i in range(10) if i not in butt]
#
# print('butt : ', butt)
# print('norm : ', norm)
#
# if n == 100:
#     print(0)
#     exit()
#
# if m == 0:
#     print(len(str(n)))
#     exit()
#
# 목표 채널의 각 자리수를, 해당 숫자를 누르기 > 숫자가 망가졌으면, 안망가진 숫자중에서 가장 차이가 적은 숫자 누르기
# 근접한 숫자 만든 후에 차이 구해서 총 자리수에 더하기
#
# num = str(n)
# count = 0
# N = ''
# for ch in num:
#     if int(ch) not in butt:   # 안 망가진 버튼인 경우
#         N += str(ch)
#     if int(ch) in butt:        # 망가진 버튼인 경우
#         tmp = 9
#         for nor in norm:
#             if tmp > abs(int(ch) - nor):
#                 tmp = abs(int(ch)- nor)
#                 tmpch = nor
#         N += str(tmpch)
#
# print(N)
#
# ans = len(str(n))
# print(ans)
# ans += abs(n - int(N))
# print(ans)