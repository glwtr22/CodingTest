# n = int(input())
# result = 0
# for num in range(1, 1000001):
#     gen = num
#     nn = num
#     while nn > 0:
#         x = nn % 10
#         nn //= 10
#         gen += x
#
#     if gen == n:
#         result = num
#         break
#
# print(result)


# 자리수 구하는 거 간결화 한 코드
n = int(input())

result = 0
for i in range(1, n+1):
    # 정수 문자열로 변환해서 iterable로 만들고 sum 함수 이용해서 간단하게 자리수 더하는 코드
    num = sum((map(int, str(i)))) + i
    if num == n:
        result = i
        break

print(result)
