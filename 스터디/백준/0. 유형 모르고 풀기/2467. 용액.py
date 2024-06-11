# [참고] https://seongonion.tistory.com/100
# 3:20 ~
# 투포인터 풀이
import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

# 포인터 초기 설정
left_idx = 0
right_idx = n-1

ans = abs(liquids[left_idx] + liquids[right_idx])
ans_left = left_idx
ans_right = right_idx

while left_idx < right_idx:
    tmp = liquids[left_idx] + liquids[right_idx]

    if abs(tmp) < ans:
        ans_left = left_idx
        ans_right = right_idx
        ans = abs(tmp)
        if ans == 0:
            break

    if tmp < 0:
        left_idx += 1
    else:
        right_idx -= 1

print(liquids[ans_left], liquids[ans_right])


# 이진 탐색 풀이 -> 시간 초과
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# liquids = list(map(int, input().split()))
#
# ans = float("INF")
# ans_left = 0
# ans_right = 0
#
# for i in range(n-1):
#     current = liquids[i]
#
#     start = i + 1
#     end = n - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#         tmp = current + liquids[mid]
#         if abs(tmp) < ans:
#             ans_left = i
#             ans_right = mid
#
#         if tmp == 0:
#             break
#
#     if tmp < 0:
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(liquids[ans_left], liquids[ans_right])



# from itertools import combinations
# n = int(input())
# val = list(map(int, input().split()))
#
# minusMin = 0
# minusMax = -1e9
# plusMin = 1e9
# plusMax = 0
#
# # 양수 혹은 음수값만 갖는 경우
# if val[0] > 0 or val[-1] < 0:
#     if val[0] > 0:
#         print(val[0], val[1])
#     else:
#         print(val[-2], val[-1])
# # 양수 음수 둘 다 존재하면
# else:
#     can = []
#     for i in range(n-1):
#         if val[i] * val[i+1] < 0:
#             minusMax = val[i]
#             plusMin = val[i+1]
#             if i != n-2:
#                 plusMin2 = val[i+2]
#                 can.append(plusMin2)
#             if i != 0:
#                 minusMax2 = val[i-1]
#                 can.append(minusMax2)
#     minusMin = val[0]
#     plusMax = val[-1]
#     can.append(minusMax)
#     can.append(minusMin)
#     can.append(plusMax)
#     can.append(plusMin)
#     can.sort()
#
#     com = combinations(can, 2)
#     result = 1e9
#     for x, y in com:
#         if abs(x + y) < result:
#             result = abs(x + y)
#             reX, reY = x, y
#
#     print(reX, reY)




'''
1) 양수 음수 둘 다 존재할 때
가장 작은 음수
가장 큰 음수
가장 작은 양수
가장 큰 양수

절댓값이 가장 작은 양수 혹은 음수 2개 더하기

2) 양수만 존재할 때
3) 음수만 존재할 때
'''

# 조합 풀이 -> 시간 초과
# from itertools import combinations
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# val = list(map(int, input().split()))
#
# com = combinations(val, 2)
#
# minVal = 1e9
# for a, b in com:
#     if minVal > abs(a + b):
#         minVal = abs(a + b)
#         mina, minb = a, b
#
# print(mina, minb)




'''
산성 양수, 알칼리성 음수
혼합 용액 특성값은 합
특성값이 0에 가까운 용액을 만들려고 한다
산성 + 산성, 알칼리성 + 알칼리성으로 특성값이 0에 가장 가까운 용액을 만들 수도 있음
특성값은 정렬되어 입력, 값이 다 다름, 산성만 혹은 알칼리성만 주어지기도 함
'''