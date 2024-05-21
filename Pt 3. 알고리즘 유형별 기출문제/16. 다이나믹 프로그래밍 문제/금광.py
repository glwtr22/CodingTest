for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])  # 배열 일정한 길이로 자를 떄 인덱스 활용
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:  # 범위 벗어나지 않게
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            # 왼쪽 아래에서 오는 경우
            if i == n - 1:  # 범위 벗어나지 않게
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]  # 범위 제약 없음

            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):  # 각 행의 마지막 원소(마지막 누적)에 대해서 최댓값 구하기
        result = max(result, dp[i][m-1])

    print(result)



# T = int(input())
# for _ in range(T):
#     n, m = map(int, input().split())
#     gold = map(int, input().split())
#     row = []
#     graph = []
#     i = 0
#     for g in gold:
#         row.append(g)
#         i += 1
#         if i == m:
#             graph.append(row)
#             row = []
#             i = 0
#
#     # 금광 최댓값 구하기
#

