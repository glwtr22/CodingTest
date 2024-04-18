# n, k = map(int, input().split())
#
# cnt = 0
# while bin(n).count('1') > k:
#     n += 1
#     cnt += 1
#
# print(cnt)

n, k = map(int, input().split())
answer = 0
while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1')
    answer += 2**idx
    n += 2**idx

print(answer)


# import heapq
#
# n, k = map(int, input().split())
#
# answer = -1
#
# if n < k:
#     answer = k - n
# elif n == k:
#     answer = 0
#
# else: # n > k
#     size = 1
#     cnt = 0
#     while True:
#         if n % 2 == 0:
#             n //= 2
#             size += 1
#         else:
#             if n // 2 >= k:
