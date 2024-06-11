N = int(input())

building = []
for _ in range(N):
    building.append(int(input()))

stack = []
result = 0

for b in building:
    while stack and stack[-1] <=b:
        stack.pop()  # 자신보다 큰 빌딩이 나왔으므로 그 이후 다 못봄
    stack.append(b)
    result += len(stack) - 1  # result에 더해주는 값은 i번째 건물을 볼 수 있는 다른 건물의 수

print(result)




# ans = [0] * N
#
# for i in range(N):
#     cnt = 0
#     for j in range(i+1, N):
#         if building[i] <= building[j]:
#             ans[i] = cnt
#             break
#         cnt += 1
#         if j == N-1:
#             ans[i] = cnt
#
# # print(ans)
# print(sum(ans))
