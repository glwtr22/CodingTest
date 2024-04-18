n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵 d 선언
d = [[0]*m for _ in range(n)]  # 2차원 리스르 선언 시, 리스트컴프리헨션 사용하는 법 기억하기 !

x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 시작 위치를 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서  방향 정의  (문제에서 북동남서 가 각각 0, 1, 2, 3 이라고 줬으므로 인덱스를 맞춰서 dx, dy 초기화)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면, 뒤로 이동
        if array[nx][ny] == 0:  # 뒤가 육지인 경우, 뒤로 이동
            x = nx
            y = ny
        else:                   # 뒤가 바다인 경우, 움직임 멈춤
            break
        turn_time = 0

print(count)

# 코드 안보고 다시 풀어보기