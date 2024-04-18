r, c = map(int, input().split())
mat = []
for _ in range(r):
    mat.append(list(input()))
alp = set()
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global answer
    #실행된 모든 dfs들 중에서 count와 현재 answer 중 큰 값으로 갱신
    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not mat[nx][ny] in alp:
            alp.add(mat[nx][ny])
            dfs(nx, ny, count+1)
            alp.remove(mat[nx][ny])

alp.add(mat[0][0]) # 좌측 상단 시작값 넣고 Dfs 시작
dfs(0, 0, 1)
print(answer)