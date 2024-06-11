# # 5:20~
# # 집합 자료구조 활용 문제
# n, m = map(int, input().split())
# parent = [0] * (n+1)  # parent 변수 1차원 리스트
#
# for i in range(n+1):
#     parent[i] = i
#
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] =  find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, a, b):
#     a_parent = find_parent(parent, a)
#     b_parent = find_parent(parent, b)
#     if a_parent < b_parent:
#         parent[b_parent] = a_parent
#     else:
#         parent[a_parent] = b_parent
#
# check = []
# for _ in range(m):
#     op, a, b = map(int, input().split())
#     if op == 0:
#         union_parent(parent, a, b)
#     else:
#         check.append((op, a, b))
#
# for c in check:
#     o, one, two = c
#     if parent[one] == parent[two]:
#         print("YES")
#     else:
#         print("NO")


# 5:20~
# 집합 자료구조 활용 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [0] * (n+1)  # parent 변수 1차원 리스트

for i in range(n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(parent, a, b)
    else:
        # 같은 집합 여부 확인할 때도, parent 배열 사용하지 않고 find_parent 함수 사용해야 함
        #     -> WHY??? : 부모 테이블 값이 같이 않아도 같은 집합일 수 있음
        # (부모 테이블이 최상위 부모 노드 저장하는게 아니라 바로 위에 부모 저장하는 테이블이라서)
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
