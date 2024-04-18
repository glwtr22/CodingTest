n = int(input ())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향 (세로축이 x , 가로축이 y 라고 생각)
# 인덱스가 같게 리스트에 저장해 둔 다음에 같은 인덱스로 접근하는 방식 기억하기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveType = ['L', 'R', 'U', 'D']

for plan in plans:   # plan in plans 처럼 꼭 i, j와 같은 문자를 사용해 for문을 돌리지 않아도 된다.
    for i in range(len(moveType)):
        if plan == moveType[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)