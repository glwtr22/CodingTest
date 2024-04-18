N = int(input())
t = []
p = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

for i in range(N-1, -1, -1):
    if i + t[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i + t[i]] + p[i])

print(dp[0])


# # 보텀업
# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# schedule = [list(map(int, input().split())) for i in range(N)]
# dp = [0 for i in range(N+1)]
#
# for i in range(N):
#     for j in range(i+schedule[i][0], N+1):
#         if dp[j] < dp[i] + schedule[i][1]:
#             dp[j] = dp[i] + schedule[i][1]
#
# print(dp[-1])  # 리스트의 뒤쪽 원소를 출력하고 싶으면 음수 인덱스로 접근
#
#
# # 탑다운
# N = int(input())
# li = [list(map(int, input().split())) for _ in range(N)]
# dp = [0 for _ in range(N+1)]
#
# for i in range(N-1, -1, -1):  # N-1부터 0까지 한 칸씩 내려오면서
#     if i + li[i][0] > N:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1], li[i][1] + dp[i + li[i][0]])





# # DP
# import sys
# input = sys.stdin.readline
#
# data = []
# n = int(input())
# for _ in range(n):
#     data.append(list(map(int, input().split())))
#
# d = [0] * (n+1)
# for i in range(1, n+1):
#     t, p = data[i-1][0], data[i-1][1]
#     # i일째에 시작한 상담이 끝나는 날 (i+t-1)을 기준으로 i-1일까지의 최대 상담 비용에 이번 상담 비용을 더한 값들 중 큰 값으로 갱신
#     if i+t-1 <= n:
#         d[i+t-1] = max(d[i+t-1], d[i-1] + p)
#     # d[i]가 d[i-1]보다 작을 경우는 i-1일째까지만 상담하는 것이 더 이득이므로 d[i]를 d[i-1]값으로 대체
#     if d[i] < d[i-1]:
#         d[i] = d[i-1]
#
# print(max(d))



# n = int(input())  # n <= 15
#
# con = []
# result = []
# for _ in range(n):
#     con.append(tuple(map(int, input().split())))
#
# for i in range(n):
#     total = 0
#     time, pay = con[i][0] - 1, con[i][1]
#     total += pay
#     for j in range(i + 1, n):
#         time -= 1
#         if time == 0 and j != n-1:
#             time, pay = con[j+1][0] - 1, con[j+1][1]
#             if j + time < n:
#                 total += pay
#                 print("더해지는 수당 : ",pay)
#                 print("총 수당 :", total)
#     result.append(total)
#
# print(result)
print(max(result))
