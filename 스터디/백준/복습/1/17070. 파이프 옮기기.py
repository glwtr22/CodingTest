n = int(input())
graph = [[] for _ in range(n)]
result = 0
for i in range(n):
    graph[i] = list(map(int, input().split()))

def dfs(position):
    global result
    # dir 2: 대각선, 1: 가로, 0: 세로
    x, y, dir = position
    if x == n-1 and y == n-1:
        result += 1
        return
    if x + 1 < n and y + 1 < n:
        if graph[x+1][y+1] == 0 and graph[x][y+1] == 0 and graph[x+1][y] == 0:
            dfs((x+1, y+1, 2)) # 대각선 이동

    if dir == 0 or dir == 2:
        if y + 1 < n:
            if graph[x][y+1] == 0:
                dfs((x, y+1, 0))

    if dir == 1 or dir == 2:
        if x + 1 < n:
            if graph[x+1][y] == 0:
                dfs((x+1, y, 1))

dfs((0, 1, 0)) # 시작 정보

print(result)



# n = int(input())
# mat = [list(map(int, input().split())) for _ in range(n)]
#
# # 이동 시킬 수 없는 경우에는 0 출력
# def dfs(x, y, i, j, mat):
#     global count
#     if i == n - 1 and j == n - 1:
#         count += 1
#         return
#
#     if i - x == 0 and j - y == 1:  # 가로로 놓여있음
#         if j + 1 < n and mat[i][j + 1] == 0:
#             dfs(i, j, i, j + 1, mat)
#             if i + 1 < n and mat[i + 1][j] == 0 and mat[i + 1][j + 1] == 0:
#                 dfs(i, j, i + 1, j + 1, mat)
#
#     elif i - x == 1 and j - y == 0:
#         if i + 1 < n and mat[i + 1][j] == 0:
#             dfs(i, j, i + 1, j, mat)
#             if j + 1 < n and mat[i][j + 1] == 0 and mat[i + 1][j + 1] == 0:
#                 dfs(i, j, i + 1, j + 1, mat)
#
#     else:  # 대각선으로 놓여 있음
#         if i + 1 < n and mat[i + 1][j] == 0:
#             dfs(i, j, i + 1, j, mat)
#         elif j + 1 < n and mat[i][j + 1] == 0:
#             dfs(i, j, i, j + 1, mat)
#         elif i + 1 < n and j + 1 < n and mat[i + 1][j + 1] == 0:
#             dfs(i, j, i + 1, j + 1, mat)
#
#
#
# count = 0
# dfs(1, 1, 1, 2, mat)
#
# print(count)