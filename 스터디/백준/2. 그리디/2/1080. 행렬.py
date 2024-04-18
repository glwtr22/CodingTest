import sys

n, m = map(int, sys.stdin.readline().split())
a = []
b = []
for _ in range(n):
    a.append([int(ch) for ch in sys.stdin.readline().strip()])
for _ in range(n):
    b.append([int(ch) for ch in sys.stdin.readline().strip()])

def flip(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            if a[i][j] == 1:
                a[i][j] = 0
            else:
                a[i][j] = 1

cnt = 0
for i in range(n-2):  # range(-1) 에 대한 처리는 ??
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            cnt += 1

print(cnt if a == b else -1)

# 맨 왼쪽 위에 있는 요소가 B 행렬과 다르면 연산 수행
