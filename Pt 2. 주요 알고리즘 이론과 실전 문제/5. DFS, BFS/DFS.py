# DFS 메소드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")       # 탐색 결과 출력
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드의 방문 여부 저장하는 1차원 리스트
visited = [False] * 9

# dfs 호출
dfs(graph, 1, visited)