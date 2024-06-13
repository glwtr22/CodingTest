# 전형적인 최소신장트리 문제 `크루스칼`
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    edges = []
    result = 0
    total_cost = 0
    parent = [0] * m

    for i in range(m):
        parent[i] = i

    for _ in range(n):
        a, b, cost = map(int, input().split())
        total_cost += cost
        edges.append((cost, a, b))

    edges.sort()  # 비용을 기준으로 오름차순 정리 -> 적은 비용부터 추가해서 최소 비용이 될 수 있도록

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    # 인덴트 잘 지키기
    print(total_cost - result)

'''
m = 0 and n = 0이면 입력 끝
도로는 양방향
도시는 항상 연결 그래프 (어떤 두 집을 골라도 왕래할 수 있는 경로가 있다)
두 집 사이 왕래 시, 불이 켜진 길만으로 서로 왕래 가능
일부 소등하려고 할 때, 절약할 수 있는 최대 액수
'''