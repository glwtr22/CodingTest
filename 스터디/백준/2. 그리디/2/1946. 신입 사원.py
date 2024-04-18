import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(input())
    score = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        score.append((a, b))
    _score = sorted(score)

    cnt = 1
    second = _score[0][1]
    for i in range(1, n):
        if _score[i][1] < second:
            cnt += 1
            second = _score[i][1]

    print(cnt)

# 튜플에서 하나의 요소를 기준으로 정렬
# 처음 면접 점수를 기준으로 리스트를 훑으면서 처음 면접 점수보다 큰 점수가 있으면 제거



# import sys
#
# T = int(sys.stdin.readline())
# for _ in range(T):
#     n = int(input())
#     score = []
#     for _ in range(n):
#         a, b = map(int, sys.stdin.readline().split())
#         score.append((a, b))
#     _score = sorted(score)
#
#     idx = 0
#     while idx < len(_score):
#         tmp = idx + 1
#         while tmp < len(_score):
#             if _score[idx][1] < _score[tmp][1]:
#                 del _score[tmp]
#             else:
#                 tmp += 1
#         idx += 1
#     print(len(_score))