import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = input().rstrip()  # 엔터 제거

stack = []
for number in numbers:
    while stack and stack[-1] < number and k > 0:
        stack.pop()
        k -= 1
    stack.append(number)

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))




# n, k = map(int, input().split())
# num = input()
#
# count = 0
# flag = 0
# for n in range(1, 11):
#     while True:
#         idx = num.index(str(n))
#         if idx == -1:
#             break
#
#         if idx != len(num)-1:
#             for i in range(idx + 1, len(num)):
#                 idx_n = num[idx]
#                 num_n = num[idx]
#                 if idx_n < num_n:
#                     count += 1
#                     tmp = ''
#                     tmp2 = ''
#                     if idx != 0:
#                         tmp = num[:idx]
#                     tmp2 = num[idx+1:]
#                     num = tmp + tmp2
#                     print(len(num))
#                     if count == k:
#                         print(num)
#                         exit(0)
