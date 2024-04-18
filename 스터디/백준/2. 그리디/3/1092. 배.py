# 가장 최선의 경우를 먼저 따지기 : 크레인이 남아있는 박스 중 가장 무거운 박스를 옮길 수 있는지 확인
# 가장 큰 무게를 드는 크레인이 가장 무거운 박스를 못옮기면 -> 불가능한 경우, -1 반환
# -1이 아닌 경우, while문을 돌면서

import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

cnt = 0
if box[0] > crane[0]: # 가장 큰 중량을 들 수 있는 크레인이 가장 큰 박스를 들지 못할 경우
    print(-1)
    exit(0)

while box:
    for c in crane:
        for b in box:
            if c >= b: # 현재 크레인이 박스를 들 수 있으면
                box.remove(b)
                break  # box 반복문 탈출 -> 다음 crane으로 이동
    cnt += 1
print(cnt)




# n = int(input())
# crane = list(map(int, input().split()))
# m = int(input())
# box = list(map(int, input().split()))
#
# crane.sort()
# box.sort()
#
# cnt = 0
# c_idx = 0
# b_idx = 0
#
# while True:
#     #print(cnt)
#     # 첫 크레인이 들려고 하는 범위의 박스들 중 첫 박스를 들 수 있나 확인
#     if box[b_idx] > crane[c_idx]: # 첫 크레인이 첫 박스를 못 들면
#         while True: # 크레인 추리기
#             if c_idx == n-1: # 박스를 들 수 있는 크레인이 없음
#                 print(-1)
#                 exit(0)
#             c_idx += 1
#             if box[b_idx] < crane[c_idx]: # 들 수 있는 크레인을 만나면 크레인 추리기 중단
#                 break
#     wid = n - 1 - c_idx
#     b_idx += wid
#     if b_idx > m-1:  # 크면, 각각의 크레인이 순차적으로 박스들을 들 수 있나 확인
#         flag = 0
#         b_idx -= wid
#         for i in range(b_idx, m):
#             if box[i] > crane[c_idx]:
#                 flag = 1
#                 break
#             if i != m-1:
#                 c_idx += 1
#             cnt += 1
#         if flag == 1:
#             continue
#         cnt += 1
#         break
#
#     if box[b_idx] > crane[n-1]:
#         print(-1)
#         exit(0)
#
#     cnt += 1
#     if b_idx == m-1:
#         break
#     b_idx += 1
#
#
# print(cnt)