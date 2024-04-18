n, m = map(int, input().split())
location = list(map(int, input().split()))

minus = []
plus = []
ans = 0
for i in range(n):
    if location[i] < 0:
        minus.append(location[i])
    else:
        plus.append(location[i])

minus.sort(reverse = True)  # 음수는 내림차순 정렬 (절댓값(거리)이 큰 게 뒤로 가게 정렬)
plus.sort()  # 양수는 오름차순 정렬

# 가장 큰 수 구하기
if len(minus) == 0:
    max_num = max(plus)
elif len(plus) == 0:
    max_num = -min(minus)
else:
    max_num = max(max(plus), -min(minus))

while minus:
    for i in range(m):
        if len(minus) == 0:
            break
        if i == 0:
            ans -= minus.pop() * 2
        else:
            minus.pop()

while plus:
    for i in range(m):
        if len(plus) == 0:
            break
        if i == 0:
            ans += plus.pop() * 2
        else:
            plus.pop()

print(ans - max_num)




# n, m = map(int, input().split())
# book = list(map(int, input().split()))
#
# total = 0
# right = []
# left = []
#
# for b in book:
#     if b > 0:
#         right.append(b)
#     else:
#         left.append(abs(b))
#
# right.sort(reverse = True)
# left.sort(reverse = True)
# print(right)
# print(left)
#
# if len(right) > 0 and len(left) > 0:
#     if right[0] >= left[0]:
#         total += right[0]
#     else:
#         total += left[0]
#
#     tmp = m
#     while tmp < len(right):
#         total += right[tmp] * 2
#         tmp += m
#     # else:
#     #     tmp = 0
#     #     total += right[tmp] * 2
#     print(total)
#
#     tmp = m
#     while tmp < len(left):
#         total += left[tmp] * 2
#         tmp += m
#     else:
#         tmp = 0
#         total += left[tmp] * 2
#
# else:
#
#
# print(total)