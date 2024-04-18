from itertools import combinations, product
import sys
input = sys.stdin.readline

n = int(input())
st = [list(map(int, input().split())) for _ in range(n)]
p = [i for i in range(1, n+1)]

def teamSt(l):
    per = list(combinations(l, 2))
    tmp = 0
    for pp in per:
        a, b = pp
        if a == b:
            continue
        team1 = st[a-1][b-1] + st[b-1][a-1]
        tmp += team1
    return tmp


result = []
per = list(combinations(p, n//2))  # 가능한 팀 조합
for p in per:
    l = list(p)
    ll = [i for i in range(1, n+1) if i not in l]
    team1 = teamSt(l)
    team2 = teamSt(ll)
    result.append(abs(team2-team1))

print(min(result))




import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [False for _ in range(n)]
min_value = sys.maxsize

def backTracking(depth, idx):
    global min_value
    if depth == n // 2:     # n은 늘 짝수 / 주어진 수의 절반이 한 팀으로 선택 되었을 때, 가지치기 시작
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:   # True 값을 가지는 팀의 능력치 power1에 합산
                    power1 += graph[i][j]
                elif not visit[i] and not visit[j]:     # False 값을 가지는 팀의 능력치 power2에 합산
                    power2 += graph[i][j]

        min_value = min(min_value, abs(power1-power2))  # 능력치 차이가 이미 저장된 변수보다 작으면 갱신
        return

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            backTracking(depth+1, i+1)      # 같은 번호 중복을 막기 위한 idx+1 인덱스로 재귀 호출
            visit[i] = False


backTracking(0, 0)
print(min_value)