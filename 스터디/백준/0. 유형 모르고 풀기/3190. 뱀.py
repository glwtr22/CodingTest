from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))

# 왜 딕셔너리로 방향 전환 시점을 저장하는 거지 ?????????????????
for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

x, y = 0, 0  # 시작 지점 왼쪽 상단
graph[x][y] = 1  # 시작 지점에 뱀 위치
cnt  = 0  # 시작 시간 0초
direction = 0  # 동쪽 바라보며 시작 -> dx, dy 변수도 동쪽을 시작으로 시계 방향(오른쪽) 회전 순서로 선언

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1 ) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1  # cnt가 시간
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    # 사과를 먹은 경우
    if graph[x][y] == 2:
        graph[x][y] = 1  # 사과 자리 뱀으로 처리
        queue.append((x, y))  # 뱀 몸통 큐에 저장
        if cnt in dirDict:  # ** 방향 전환 타이밍 확인 **
            turn(dirDict[cnt])

    # 사과 없고 그냥 이동인 경우
    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])

    else:  # 자신의 몸통과 부딪힌 경우
        break


print(cnt)




'''
1. 그래프 전부 0으로 채우기
2. 사과 위치는 2
3. 뱀이 차지하는 부분은 1
4. 뱀이 이동할 때마다 머리와 꼬리 한 칸씩 전진 -> 몸 길이는 그래도
5. 사과를 먹으면 머리는 전진, 꼬리는 이동 x -> 몸 길이 한 칸 늘어남
6. 방향 전환을 해야 하는 타이밍에 맞춰 방향 전환 수행

복잡한 구현 문제
=> 무엇을 구현해야 하는지를 정리 후, 하나씩 차례대로 구현

[구체적인 방법]
4. "큐를 뱀의 몸이라고 생각" -> 이동 시 큐에서 Pop, 현재 위치 push
5. pop 하지 않고, 현재 위치만 push
6. 딕셔너리를 이용해 시간을 키 값으로, 방향을 밸류값으로 입력 받기

'''



# n = int(input())
# k = int(input())
# mat = [[]]
#
# apple =[]
# for _ in range(k):
#     apple.append(tuple(map(int,input().split())))
#
# rotate = int(input())
# time = []
# for _ in range(rotate):
#     s, d = input().split()
#     s = int(s)
#     time.append((s, d))

