import sys
input = sys.stdin.readline

# i행에 배치할 퀸에 대해서, 문제 조건에 맞게 놓을 수 있는지 확인하는 함수
def promising(i):
    for k in range(i):
        # 놓으려는 열에 이미 퀸이 있거나 왼쪽 오른쪽 위 대각선에 퀸이 있는 경우
        if abs(row[i] - row[k]) == i - k:
            return False
    return True


def backtracking(i):
    global result
    if i == N:  # 모든 행에 퀸 배치한 경우
        result += 1
        return
    for j in range(N):
        if check[j]:  # j열에 퀸이 이미 놓인 경우
            continue
        row[i] = j
        if promising(i):  # 상하 대각선에 퀸이 없는 경우에만
            check[j] = True
            backtracking(i+1)
            check[j] = False  # 이 줄이 동시적으로 다른 backtracking 함수가 실행되고 있을 때 실행되는 것 ?


N = int(input())
row = [0] * N  # 각 행의 무슨 열 번호에 퀸을 놓았는 지 저장하는 변수
check = [False] * N     # 이미 퀸이 놓인 열 정보 저장하는 변수
result = 0       # 가능한 경우의 수 저장하는 변수

backtracking(0)

print(result)


'''
이후의 사건이 이전의 사건에 종속이다

체스판의 가장 첫 행부터 차례대로 퀸을 두면서 아래 행으로 이동
확인해야 하는 것은
1. 같은 열에 퀸이 있는가
2. 대각선에 퀸이 있는가
    아래 행으로 내려가면서 퀸을 놓고 있기 때문에, 현재 놓으려는 퀸의
    1) 왼쪽 대각선 위에 퀸이 있는가
    2) 오른쪽 대각선 위에 퀸이 있는가


'''