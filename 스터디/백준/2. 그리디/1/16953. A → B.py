import sys
input = sys.stdin.readline

a, b = map(int, input().split())
result = 1

while b !=a:
    result += 1
    tmp = b

    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2

    if tmp == b:
        print(-1)
        break
else:
    print(result)


# 2로 나눠지면 나누기
# 일의 자리 수가 1이면 1 제거하기

# a, b = map(int, input().split())
# cnt = 0
# while b > 0:
#     if b % 2 == 0:
#         b //= 2
#         cnt += 1
#     elif b % 10 == 1:
#         b //= 10
#         cnt += 1
#     else:
#         if a == b:
#             cnt += 1
#             break
#         cnt = -1
#         break
#     if a == b:  # 추가
#         cnt += 1
#         break
#     if b <= 0:
#         cnt = -1
#
# print(cnt)