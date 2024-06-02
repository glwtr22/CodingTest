import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

K = int(input())

def dfs(start, group):
    visited[start] = group
    for i in graph[start]:
        if not visited[i]:
            a = dfs(i, -group)
            if not a:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        # 그래프가 끊어져 있는 경우가 있을 수 있다 -> 모든 노드 탐색하면서 방문하지 않은 노드에 대해서 확인
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")