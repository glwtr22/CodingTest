from collections import deque

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    mat = []
    for i in range(h):
        mat.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    def bfs(x, y):
        queue = deque([(x, y)])
        mat[x][y] = 0
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue

                if mat[nx][ny] == 1:
                    queue.append((nx, ny))
                    mat[nx][ny] = 0

    cnt = 0
    for x in range(h):
        for y in range(w):
            if mat[x][y] == 1:
                bfs(x, y)
                cnt += 1

    print(cnt)