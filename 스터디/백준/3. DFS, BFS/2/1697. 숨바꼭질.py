from collections import deque

n, k = map(int, input().split())
max_num = 100000
visited = [0] * (max_num + 1)

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            break

        for j in (x-1, x+1, x*2):  # 반복문에서 튜플 사용
            if j < 0 or j > max_num:
                continue
            if not visited[j]:  # 파이썬에서 0만 False, 나머지 정수는 True
                visited[j] = visited[x] + 1
                queue.append(j)

bfs()