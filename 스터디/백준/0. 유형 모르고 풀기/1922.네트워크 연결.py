N = int(input())
M = int(input())

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i  # 부모 테이블 자기 자신으로 초기화

def find_parent(parent, x):  # 루트 노드 찾아주는 함수
    if parent[x] != x:  # 루트 노드가 아닌 경우
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):  # 두 원소를 같은 집합으로 합치는 함수
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:  # 관행적으로 노드 번호가 작은 것이 부모 노드가 되도록 설계
        parent[b] = a
    else:
        parent[a] = b


edges =[]
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()  # cost 기준으로 오름차순 정렬

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):   # 같은 집합에 있지 않은 경우에
        union_parent(parent, a, b)
        result += cost

print(result)


'''
모든 컴퓨터를 연결하는데 드는 최소 비용 구하기
= 최소 신장 트리
'''