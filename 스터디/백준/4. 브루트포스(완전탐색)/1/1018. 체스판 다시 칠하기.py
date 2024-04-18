n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(input())

result = []
for i in range(n - 7):
    for j in range(m - 7):
        w = 0
        b = 0
        for k in range(i, i + 8):  # range를 어떻게 적는지에 따라서 인덱스가 간단해질 수 있다
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        w += 1  # 화이트로 시작하는 경우에는 (k + l) % 2 가 화이트여야 한다
                    if board[k][l] != 'B':
                        b += 1
                else:
                    if board[k][l] != 'W':
                        b += 1
                    if board[k][l] != 'B':
                        w += 1
        result.append(b)
        result.append(w)

print(min(result))

# import copy
#
# n, m = map(int, input().split())
# _board = []
# for i in range(n):
#     _board.append(list(e for e in input()))
#
# def check(x, y, board):
#     count = 0
#     for i in range(8):
#         if i != 7 and board[x + i][0] == board[x + i + 1][0]:
#             count += 1
#             if board[x + i][0] == 'W':
#                 board[x + i + 1][0] = 'B'
#             else:
#                 board[x + i + 1][0] = 'W'
#         for j in range(7):
#             if board[x + i][y + j] == board[x + i][y + j + 1]:
#                 count += 1
#                 if board[x + i][y + j] == 'W':
#                     board[x + i][y + j + 1] = 'B'
#                 else:
#                     board[x + i][y + j + 1] = 'W'
#
#     return count
#
# result = 64
# for i in range(n - 7):
#     for j in range(m - 7):
#         board = copy.deepcopy(_board)
#         ch = check(i, j, board)
#         print(ch)
#         result = min(result, ch)
#
# print(result)
