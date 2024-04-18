import sys
n, l = map(int, input().split())
pos = list(map(int, sys.stdin.readline().split()))
pos.sort()

start = pos[0] - 0.5
end = start + l
cnt = 1

for i in range(0, len(pos)):
    if start < pos[i] < end:
        continue
    else:
        cnt += 1
        start = pos[i] - 0.5
        end = start + l

print(cnt)


# import sys
#
# n, l = map(int, input().split())
# pos = list(map(int, sys.stdin.readline().split()))
#
# pos.sort()
# wid = []  # 연달아 새는 곳의 길이만 저장할 게 아니라, (시작점, 끝점), (시작점, 길이) 등의 정보를 추가적으로 저장해야 할듯??
# w = 1
# f = 1
# for i in range(1, len(pos)):
#     if pos[i] - pos[i-1] == 1:
#         w += 1
#         if f == 1:
#             idx = i-1
#             f += 1
#
#     else:  # pos[i] - pos[i-1] != 1
#         wid.append((idx, w))
#         w = 1
#         f = 1
#
#     if i == (len(pos) - 1): # pos 리스트의 마지막 요소일 경우에 wid에 추가
#         wid.append((idx, w))
#
#
# print(wid)
# cnt = 0
# flag = 0
# tmp = 1   # 여기가 맞는지
# if l == 1:
#     cnt = sum(wid)
# else:
#     for i in range(len(wid)):
#         while tmp > 1:
#             tmp -= 1
#             flag = 1
#         if flag == 1:
#             flag = 0
#             continue
#
#         idx, ww = wid[i]
#         if ww >= l:
#             if ww % l == 0:
#                 cnt = cnt + ww // l
#             else:
#                 cnt = cnt + (ww // l + 1)
#         else: # 현재 넓이보다, 테이프 길이가 길면 (넓이가 1인 경우도 고려)
#             idx2 = idx
#             while idx2 - idx <= l:
#                 if idx == len(wid) - 1:
#                     break
#                 print('tmp : ', tmp)
#                 idx2, ww2 = wid[i + tmp]
#                 tmp += 1
#             tmp -= 1
#             idx2, ww2 = wid[i + tmp]
#             if (idx2 + ww2) - idx >= l and tmp != 0:
#                 # 인덱스 갱신
#                 wid[i + tmp][1] = idx + l + 1
#                 tmp -= 1
#
#             cnt += 1
#
# print(cnt)







    # sortedWid = sorted(wid)
    # if sortedWid[0] < l: # 제일 작은 연달아 보다 테이프 길이가 길면, 다음 연달아 까지 커버가 가능한지 체크하는 방식으로 카운트
    #     # wid를 돌면서 각 w 마다 l 보다 작은지 큰지 비교가 나은지
    #     # 아니면, 최소 w랑 l을 비교해서 판단 > 하나의 방식으로 전체 카운트 하는게 나은지..
    #     for i in range(wid):
    #         idx, ww = wid[i]
    #         if ww > l
    #
    # else:  # wid의 w 여러 개를 길이가 긴 테이프 하나로 커버가능한 경우
    #     if w % l == 0:
    #         cnt = cnt + w // l
    #     else:
    #         cnt = cnt + (w // l + 1)




# print(cnt)