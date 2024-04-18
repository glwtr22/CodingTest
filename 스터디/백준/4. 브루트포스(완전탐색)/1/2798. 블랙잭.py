# n, m = map(int, input().split())
# card = list(map(int, input().split()))
#
# total = 0
# result = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             total = card[i] + card[j] + card[k]
#             if total <= m:
#                 result = max(total, result)
#
# print(result)


#  조합 라이브러리 활용 풀이
from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for card in combinations(cards, 3):
    tmpSum = sum(card)
    if tmpSum <= m:
        result = max(result, tmpSum)

print(result)