import sys
input = sys.stdin.readline

T = int(input())

def num(M, N, x, y):
    k = y
    while k <= M * N:
        if (k - x) % M == 0:
            return k
        k += N
    return -1


for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(num(M, N, x, y))

