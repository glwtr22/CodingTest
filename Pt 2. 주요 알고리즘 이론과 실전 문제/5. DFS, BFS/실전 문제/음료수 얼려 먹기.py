n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# map 함수가 input으로 들어온 문자열의 각 요소(문자)에 int 함수를 적용 후 iterable로 반환

def dfs(x, y):
    # 주어진 범위를 벗어나면 종료
    if x <= 1 or x >= n or y <= 1 or y >= m:
        return False

    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1

        # 상하좌우의 모든 위치들 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)    # 연결된 노드에 대해서 방문처리를 하기 위함 (return 값이 사용되지는 않는다 !)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)