# 참고 : https://velog.io/@hamsangjin/%EB%B0%B1%EC%A4%80-9019%EB%B2%88-DSLR-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    # ch 리스트를 이용해 한 번 찾았던 정수는 다시 차지 않게 표시 !!!
    ch = [False for _ in range(10001)]
    A, B = map(int, input().strip().split())

    Q = deque()
    Q.append([A, ''])
    ch[A] = True

    while Q:
        n, cmd = Q.popleft()

        if n == B:
            print(cmd)
            break

        # D
        d = (2 * n) % 10000
        if not ch[d]:
            ch[d] = True
            Q.append([d, cmd + 'D'])

        # S
        s = (n - 1) % 10000  # -1 % 10000 == 9999
        if not ch[s]:
            ch[s] = True
            Q.append([s, cmd + 'S'])

        # L
        l = n // 1000 + (n % 1000) * 10
        if not ch[l]:
            ch[l] = True
            Q.append([l, cmd + 'L'])

        # R
        r = n // 10 + (n % 10) * 1000
        if not ch[r]:
            ch[r] = True
            Q.append([r, cmd + 'R'])



# # 7:25~
# from collections import deque
# T = int(input())
#
# def doD(A, B):
#     x = 2 * A % 10000
#     if x == A:
#
#     return
#
# def doS(A, B):
#     return
#
# def doL(A, B):
#     return
#
# def doR(A, B):
#     return
#
#
#
# comm = ''
# for _ in range(T):
#     A, B = map(int, input().split())
#     comm = ''
#     doD(A, B, comm + 'D')
#     doS(A, B)
#     doL(A, B)
#     doR(A, B)
#     # 백트래킹 어떻게 해 .. ?





# from collections import deque
# T = int(input())
#
# def trans(A, B, comm):
#     if A == B:
#         print(comm)
#         return
#     # 왼쪽 회전
#     a = deque(str(A))
#     x = a.popleft()
#     a.append(x)
#     # 오른쪽 회전
#     b = deque(str(A))
#     y = b.pop()
#     b.appendleft(y)
#
#     trans(2 * A % 10000, B, comm + "D")
#     trans(A - 1, B, comm + "S")
#     trans(int(''.join(a)), B, comm + "L")
#     trans(int(''.join(b)), B, comm + "R")
#     return
#
#
#
#
# comm = ''
# for _ in range(T):
#     A, B = map(int, input().split())
#
#     # 왼쪽 회전
#     a = deque(str(A))
#     x = a.popleft()
#     a.append(x)
#     #오른쪽 회전
#     b = deque(str(A))
#     y = b.pop()
#     b.appendleft(y)
#
#     trans(2 * A % 10000, B, comm + "D")
#     trans(A-1, B, comm + "S")
#     trans(int(''.join(a)), B, comm + "L")
#     trans(int(''.join(b)), B, comm + "R")




'''
D S L R 4가지 명령을 이용하는 계산기
레지스터에 n 저장 -> n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4
D : 2n mod 10000 저장
S : n-1 (0이면 9999 저장)
L : n 각 자리수를 왼편으로 회전
R : n 각 자리수를 오른편으로 회전

서로 다른 정수 A와 B에 대하여, A -> B로 바꾸는 최소한의 명령어를 생성하기
가능한 명령어 나열이 여러 개인 경우 -> 아무거나 출력
'''