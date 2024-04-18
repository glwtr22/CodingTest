n = int(input())
num = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            # dp[i]에 저장되는 값 : num[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))











'''
위 코드랑 출력 다름
첫번째 풀이
'''

# n = int(input())
# num = list(map(int, input().split()))
# dp = [0] * n
#
# for i in range(n):
#     tmp = num[i]
#     count = 1
#     for j in range(i+1, n):
#         if tmp < num[j]:
#             count += 1
#             tmp = num[j]
#     dp[i] = count

# print(max(dp))