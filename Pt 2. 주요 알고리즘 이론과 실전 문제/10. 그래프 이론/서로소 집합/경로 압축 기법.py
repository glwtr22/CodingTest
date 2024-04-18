# 서로소 집합 알고리즘에서 루트 노드를 찾아주는 find_parent 시간 복잡도 개선
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]