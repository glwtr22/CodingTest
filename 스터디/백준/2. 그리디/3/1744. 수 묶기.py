n = int(input())

plus = []
minus = []

total = 0
for i in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        total += 1

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        total += plus[i]
    else:
        total += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        total += minus[i]
    else:
        total += (minus[i] * minus[i+1])

print(total)

# 3. 아이디어 수정

# n = int(input())
# plus = []
# minus = []
# total = 0
#
# for _ in range(n):
#     num = int(input())
#     if num > 1:
#         plus.append(num)
#     elif num == 1:
#         total += 1
#     elif num < 1:
#         minus.append(num)
#
# plus.sort(reverse=True)
# minus.sort()
#
# if len(plus) != 1 and len(plus) != 0:
#     p = 0
#     while p < (len(plus) - 1):
#         if len(plus) % 2 == 1:
#             total += plus[len(plus)-1]
#         tmp = plus[p] * plus[p+1]
#         total += tmp
#         p += 2
# elif len(plus) == 1:
#     total += plus[0]
# else:
#     total += 0
#
# if len(minus) != 1 and len(minus) != 0:
#     m = 0
#     while m < (len(minus) - 1):
#         if len(minus) % 2 == 1:
#             total += minus[len(minus) - 1]
#         tmp = minus[m] * minus[m + 1]
#         total += tmp
#         m += 2
# elif len(minus) == 1:
#     total += minus[0]
# else:
#     total += 0
#
# print(total)


#2.

# n = int(input())
# num = []
# for _ in range(n):
#     num.append(int(input()))
#
# num.sort()
# # print(num)
#
# total = 0
# # while 0 in num:
# #     if num.index(0) != 0:
# #         del num[num.index(0)]
# #         del num[0]
# #     else:
# #         del num[0]
#
# while 1 in num:
#     total += 1
#     del num[num.index(1)]
# print("중간: ", total)
# print(num)
# # print(total)
#
# def cal(num):
#     idx = 0
#     total = 0
#     if num[0] > 0:
#         num.sort(reverse=True)
#     if len(num) == 1:
#         return num[0]
#
#     if len(num) % 2 == 1:
#         total += num[len(num)-1]
#     while idx < len(num)-1:
#         total += num[idx] * num[idx+1]
#         idx += 2
#     return total
#
# idx = -1
#
# #print('num :', num)
# if len(num) == 1:
#     total += num[0]
#     print(total)
#     exit(0)
#
# if len(num) == 0:
#     print(total)
#     exit(0)
#
# for i in range(len(num)-1):
#     if num[i] * num[i + 1] > 0 and num[i] < 0: # 부호가 같으면
#         continue
#     elif num[i] * num[i+1] == 0:
#         if num[i+1] == 0:
#             continue
#         else:
#             idx = i+1
#             break
#     else:
#         idx = i
#         break
# print(idx)
#
# if idx != -1:
#     if num[idx] != 0:
#         minus = num[:idx+1]
#     plus = num[idx+1:]
#     # print(minus)
#     # print(plus)
#     total += cal(plus)
#     if minus:
#         total += cal(minus)
# else:
#     total += cal(num)
#
# print(total)


#1.

# if idx != 0:
#     minus = num[:idx+1]
#     plus = num[idx+1:]
#     plus.sort(reverse=True)
#     total += cal(plus) + cal(minus)
# else: # idx == 0
#     if len(num) == 2:
#         total += num[0]
#         total += num[1]
#     else:
#         if num[i] > 0:
#             num.sort(reverse=True)
#         total += cal(num)

# print(total)