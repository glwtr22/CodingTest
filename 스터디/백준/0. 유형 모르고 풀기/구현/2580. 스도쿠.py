import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
# 채워야 하는 칸의 위치 정보 저장하는 변수
nxt = []
for x in range(9):
    for y in range(9):
        if board[x][y] == 0:
            nxt.append((x, y))

def check_h(x, a):
    for y in range(9):
        if board[x][y] == a:
            return False
    return True

def check_v(y, a):
    for x in range(9):
        if board[x][y] == a:
            return False
    return True

def check_b(x, y, a):
    x = x // 3 * 3
    y = y // 3 * 3
    for dx in range(x, x+3):
        for dy in range(y, y+3):
            if board[dx][dy] == a:
                return False
    return True


def sudoku(n):
    # 빈칸 전부 채운 경우 -> 종료
    if n == len(nxt):
        for row in range(9):
            print(*board[row])
        sys.exit(0)

    # 빈칸의 x, y 좌표
    x = nxt[n][0]
    y = nxt[n][1]
    # 가능한 모든 숫자에 대해서 ...
    for a in range(1, 10):
        if check_h(x, a) and check_v(y, a) and check_b(x, y, a):  # 전부 행, 열, 사각형에 a가 없으면
            board[x][y] = a  # 빈칸 a로 채우기
            sudoku(n+1)
            board[x][y] = 0 # 백트래킹 ?

sudoku(0)

# [참고] https://velog.io/@twoju/BOJ-2580-%EC%8A%A4%EB%8F%84%EC%BF%A0


# 완전탐색풀이 시간초과
# 12:20~
# import sys
# input = sys.stdin.readline
#
# mat = [list(map(int, input().split())) for _ in range(9)]
#
# def fillBlock(x, y):
#     numSet = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
#     # 1. 행 체크
#     for i in range(9):
#         if i != y:
#             if mat[x][i] in numSet:
#                 numSet.remove(mat[x][i])
#     # 2. 열 체크
#     for i in range(9):
#         if i != x:
#             if mat[i][y] in numSet:
#                 numSet.remove(mat[i][y])
#
#     # 3. 포함된 정사각형 체크
#     xm = x // 3
#     ym = y // 3
#     for i in range(3):
#         for j in range(3):
#             xx = xm * 3 + i
#             yy = ym * 3 + j
#             if xx != x and yy != y:
#                 if mat[xx][yy] in numSet:
#                     numSet.remove(mat[xx][yy])
#
#     if len(numSet) == 1:
#         n = list(numSet)
#         mat[x][y] = n[0]
#
# while True:
#     for i in range(9):
#         for j in range(9):
#             if mat[i][j] == 0:
#                 fillBlock(i, j)
#     zero = 0
#     for k in range(9):
#         zero += mat[k].count(0)
#     if zero == 0:
#         break
#
#
# for i in range(9):
#     for j in range(9):
#         print(mat[i][j], end=' ')
#     print()

'''
게임 시작 전 스도쿠 판에 쓰여 있는 숫자들 주어질 때
모든 빈 칸이 채워진 최종 모습 출력하기
'''
