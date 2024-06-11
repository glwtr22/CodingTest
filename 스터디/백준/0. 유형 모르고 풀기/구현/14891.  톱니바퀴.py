# 9:15 ~
import sys
from collections import deque
import copy
input = sys.stdin.readline

gears = []
for _ in range(4):
    gears_str = str(input().rstrip())
    gears.append(deque([int(i) for i in gears_str]))

K = int(input())
do = []
for i in range(K):
    do.append(list(map(int, input().split())))

def can_turn_left(num, l):
    if num < 0:  # 왼쪽 톱니바퀴가 없으면
        return False
    if gears[num][2] != l: # 극이 다를 때 회전
        return True
    return False  # 그 이외 경우 false 출력

def can_turn_right(num, r):
    if num > 3:  # 오른쪽 톱니바퀴가 없으면
        return False
    if gears[num][6] != r: #극이 다를 때 회전
        return True
    return False  # 그 외 경우 False 출력

# 인덱스 2가 오른쪽, 6이 왼쪽
def what_dir_turn(num, dir):
    if num > 3 or num < 0:
        return
    r, l = gears[num][2], gears[num][6]
    turn(num, dir)  # 회전
    visited[num] = True  # 방문 처리
    if can_turn_right(num+1, r) and visited[num + 1] == False:
        what_dir_turn(num+1, -dir)
    if can_turn_left(num-1, l) and visited[num - 1] == False:
        what_dir_turn(num-1, -dir)
    return

# deque의 rotate 함수 활용
def turn(num, dir):
    if dir == 1:
        gears[num].rotate(1)
    else:
        gears[num].rotate(-1)


for num, dir in do:
    visited = [False for _ in range(4)]
    what_dir_turn(num-1, dir)

answer = 0
if gears[0][0] == 1:
    answer += 1
if gears[1][0] == 1:
    answer += 2
if gears[2][0] == 1:
    answer += 4
if gears[3][0] == 1:
    answer += 8
print(answer)


'''
톱니바퀴 돌리기
오른쪽, 왼쪽 톱니가 돌아가는가 확인
만약 돌아가면 돌리기
명령을 모두 수행한 후 점수 계산
'''

'''
회전은 한 칸 기준
회전하는 톱니바퀴와 맞닿은 톱니의 극이 '다르면'
회전한 방향과 반대방향으로 회전한다

1이 시계, -1이 반시계
각 톱니의 12시 방향이 N극이면 0점 S극이면 1~4번 순서대로 1 2 4 8점

최종 톱니바퀴 상태 구하기 
'''