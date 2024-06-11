from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
distance = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()

def bfs(Dx, Dy):
    while queue: # 고슴도치 초기 위치랑, 초기 물 위치 들어 있는 상태로 시작
        x, y = queue.popleft()
        # 종료 조건 : 고슴도치가 굴에 도착했을 때
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]  # 걸린 시간 반환
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 고슴도치 먼저 이동 => '빈칸' 혹은 '굴' 일 때 이동
                if graph[x][y] == 'S' and (graph[nx][ny] == .' 'or graph[nx][ny] == 'D'):
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                # 물이면 => 빈칸 혹은 고슴도치 이동 전 위치인 경우에 이동
                elif graph[x][y] == '*' and (graph[nx][ny] == '.' or graph[nx][ny] == 'S'):
                    graph[nx][ny] = '*'
                    queue.append((nx, ny))

    return "KAKTUS"

for x in range(n):
    for y in range(m):
        # 고슴도치 위치 저장
        if graph[x][y] == 'S':
            queue.append((x, y))
        # 굴의 위치 저장
        elif graph[x][y] == 'D':
            Dx, Dy = x, y

for x in range(n):
    for y in range(m):
        if graph[x][y] == '*':
            queue.append((x, y))

print(bfs(Dx, Dy))


# [참고] https://wookcode.tistory.com/167

# #9:40~
# r, c = map(int, input().split())
# graph = []
# for _ in range(r):
#     graph.append(list(map(int, input().split())))




'''
빈 곳은 .  물 찬 곳은 *  돌은 X
비버의 굴 D, 고슴도치의 위치 S
매 분마다
    - 고슴도치는 현재 칸과 인접한 네 칸 중 하나로 이동 가능
    - 물도 비어 있는 칸으로 확장
    
물과 고슴도치는 돌 통과 못함
고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소한의 시간
'''