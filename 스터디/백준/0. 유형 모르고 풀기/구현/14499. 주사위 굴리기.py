n, m, x, y, k = map(int, input().split())

board = []
#동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: # 동쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2: # 서쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3: # 북쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:  # 남쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in range(n):
    board.append(list(map(int, input().split())))

comm = list(map(int, input().split()))

nx, ny = x, y
for c in comm: # k 개의 명령 순회
    nx += dx[c-1]
    ny += dy[c-1]
    # 해당 명령을 수행 했을 때 지도상에 위치하는지 확인
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[c-1]
        ny -= dy[c-1]
        continue
    # 주사위를 굴려도 지도를 벗어나지 않는 경우
    turn(c)  # 주사위 굴리고
    # 작업 수행
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]  # 지도 칸이 0인 경우, 주사위 밑바닥 숫자를 해당 칸에 복사
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])


'''
인덱스 [1, 2, 3, 4, 5, 6] 각각의 인덱스가 [위쪽, 뒤쪽, 오른쪽, 왼쪽, 앞쪽, 바닥] 이라고 했을 떄
동쪽으로 굴리면, [3, 2, 6, 1, 5, 4]로 변한다
=> 나머지 방향에 대해서도 어떻게 변화하는지 파악하면 문제를 풀 수 있다.
[참고] https://hongcoding.tistory.com/128
'''

'''
"처음에 주사위에는 모든 면에 0 적혀 있다"
지도의 각 칸에는 정수가 적혀 있음
이동한 칸에 0이 적혀 있으면, 주사위 바닥면에 적혀 있는 수가 해당 칸에 복사
이동한 칸이 0이 아니면, 바닥에 적힌 수가 주사위에 복사 + 해당 칸에 적힌 수 0

주사위는 지도 바깥으로 이동 불가능
바깥으로 이동하려는 경우 해당 명령 무시 및 출력 X
명령 -> 1, 2, 3, 4 순서대로 동 서 북 남

이동할 떄마다 주사위 윗면에 적힌 수 출력
'''