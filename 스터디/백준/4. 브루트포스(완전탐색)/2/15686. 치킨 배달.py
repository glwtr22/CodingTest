from itertools import combinations
import sys
input =  sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
# 집, 치킨집 위치 저장
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i+1, j+1))
        if city[i][j] == 2:
            chicken.append((i+1, j+1))

result = []
# m개의 치킨집 선택
per = list(combinations(chicken, m))
for i in range(len(per)):
    dist = 0
    for k in range(len(house)):
        tmp = 101  # 50 + 50 보다 1 큰 값
        for j in range(m):
            tmp = min(tmp, abs(per[i][j][0] - house[k][0]) + abs(per[i][j][1] - house[k][1]))
        dist += tmp
    result.append(dist)

print(min(result))