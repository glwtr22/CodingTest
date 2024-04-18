n = int(input())
count = 0
for num in range(1, n+1):
    numStr = list(map(int, str(num)))
    if num < 100:
        count += 1
    elif numStr[2] - numStr[1] == numStr[1] - numStr[0]:
        count += 1


print(count)



# n = int(input())
# count = 0
# for num in range(1, n+1):
#     numStr = list(map(int, str(num)))
#     N = len(numStr)
#     if N :
#         count += 1
#         continue
#     for j in range(N):
#         tmp = 1
#         if j == 0:
#             sub = numStr[j + 1] - numStr[j]
#         if j < len(numStr) - 1:
#             if numStr[j+1] - numStr[j] == sub:
#                 tmp += 1
#     if tmp == len(numStr) - 1:
#         print(numStr)
#         count += 1
#
#
# print(count)