import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * M for _ in range(N)]
answer = 0

# 이차원 배열 board의 각 행에 max 함수를 씌워 최댓값을 구하고, 그 최댓값들 중 최댓값을 구하기
# 이차원 배열 board에 저장된 값들 중 최댓값 구하기
max_val = max(map(max, board))

def dfs(x, y, step, total):
    global answer

    # 더 최적화를 위한 조건문 (굳이 안써도 되긴 함)
    if total + max_val*(4-step) <= answer:
        return

    if step == 4:
        answer = max(answer, total)
        return

    for dx, dy in d:  # 튜플인 원소를 for 문 안에서 바로 분해 가능 !
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            # 'ㅗ' 모양에 대한 탐색
            if step == 2:
                visited[nx][ny] = True
                # dfs의 1,2번 인자로 nx, ny가 아닌 x, y를 넣어줌으로써 2번쨰 블록까지 이어 붙였을 때, 새로운 블록을 이어붙일 다음 블록을 탐색하지 않고 다시 기존 블록 위치에서 탐색
                dfs(x, y, step + 1, total + board[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, step+1, total + board[nx][ny])
            visited[nx][ny] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(answer)


# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def check(i, j, total, cnt):
#     global maxTotal
#
#     if cnt == 4:
#         maxTotal = max(maxTotal, total)
#         return
#
#     for k in range(4):
#         nx = i + dx[k]
#         ny = j + dy[k]
#         if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
#             visited[nx][ny] = True
#             check(nx, ny, total + arr[nx][ny], cnt + 1)
#             visited[nx][ny] = False  # 'ㅗ' 모양을 제외한 테트로미노 각각에 대해 가능한 모든 경우를 확인하기 위한 백트래킹
#
# def exce(i, j):
#     global maxTotal
#     for k in range(4):
#         tmp = arr[i][j]
#         for l in range(3):
#             t = (k+l)%4
#             nx = i + dx[t]
#             ny = j + dy[t]
#
#             if not (0 <= nx < n and 0 <= ny < m):
#                 tmp = 0
#                 break
#             tmp += arr[nx][ny]
#
#         maxTotal = max(maxTotal, tmp)
#
#
# maxTotal = 0
# for i in range(n):
#     for j in range(m):
#         cnt = 1
#         total = arr[i][j]
#         visited[i][j] = True
#         check(i, j, total, cnt)
#         visited[i][j] = False  # 시작점의 모든 경우를 확인하기 위한 백트래킹
#
#         exce(i, j)
#
# print(maxTotal)

'''
틀은 맞게 짰는데
1. visited 변수로 방문 여부를 관리해야 하는 이유
2. 'ㅗ' 모양 에 대한 함수

https://cijbest.tistory.com/87
'''