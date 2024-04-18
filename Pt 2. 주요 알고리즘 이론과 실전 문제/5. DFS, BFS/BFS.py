from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])      # deque 선언과 초기화 하고 싶으면 [요소, 요소 ...] 형태로 인자 주기
    visited[start] = True

    # 파이썬에서 빈 리스트는 False로 간주되고, 비어 있지 않은 리스트는 True로 간주됩니다.
    # 따라서, While queue는 큐가 빌 때까지 반복하라는 의미 !
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

# bfs 호출
bfs(graph, 1, visited)