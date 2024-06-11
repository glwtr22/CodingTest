#11:15~
import sys
input = sys.stdin.readline

r, c, T = map(int, input().split())
room = []
for _ in range(r):
    room.append(list(map(int, input().split())))

def spread():
    # 각 지점의 미세먼지 확산량 저장하는 변수 d
    d = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] != -1 and room[i][j] != 0:
                d[i][j] = room[i][j] // 5
                count = 0
                for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        count += 1
                room[i][j] = room[i][j] - count * d[i][j]


    # d[i][j]의 확산량을 주변으로 누적하는 부분
    for i in range(r):
        for j in range(c):
            if d[i][j] != 0:
                for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        room[nx][ny] += d[i][j]
def clean():
    for i in range(r):
        if room[i][0] == -1:
            t = i-1
            b = i+2
            break

    # 위 반시계 순환
    for i in range(t, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(c-1):
        room[0][i] = room[0][i+1]
    for i in range(0, t+1):
        room[i][c-1] = room[i+1][c-1]
    for i in range(c-1, 1, -1):
        room[t+1][i] = room[t+1][i-1]
    # 공기 청정기에서는 공기 정화되어서 나옴
    room[t+1][1] = 0

    # 아래 시계 순환
    for i in range(b, r-1):
        room[i][0] = room[i+1][0]
    for i in range(c-1):
        room[r-1][i] = room[r-1][i+1]
    for i in range(r-1, b-1, -1):
        room[i][c-1] = room[i-1][c-1]
    for i in range(c-1, 1, -1):
        room[b-1][i] = room[b-1][i-1]
    room[b-1][1] = 0

time = 0
while True:
    if time == T:
        break
    spread()
    clean()
    time += 1

total = 0
for i in range(r):
    total += sum(room[i])

print(total+2)



# print()
    # for i in range(r):
    #     print(*room[i])
'''
1. 미세먼지 확산
2. 공기청정기 작동
'''

'''
공기청정기는 항상 1번 열에 위치
1초 동안 일어나는 일
1. 미세먼지 확산 (모든 칸에서 동시에 발생)
    공기청정기가 없고 칸이 있는 인접한 네 칸으로 확산
    확산되는 양은 A/5버림 만큼 확산
    확산되고 남은 미세먼지 양은 A - A/5 * (확산된 방향의 개수)
    
2. 공기청정기 작동
    윗 부분은 반시계 방향 순환, 아래 부분은 시계 방향 순환
    바람이 불면 미세먼지가 모두 방향대로 한 칸씩 이동
    공청 바람은 미세먼지 X, 공기청정기로 들어간 미세먼지는 모두 정화
'''