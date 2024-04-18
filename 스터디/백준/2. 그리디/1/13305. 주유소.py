import sys
n = int(input())
road = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))

price = city[0]
liter = road[0]
cost = 0
for i in range(1, n):
    if price > city[i] or i == n-1:  # 더 져렴한 도시 도착한 경우 or 마지막 도시까지 도달한 경우
        cost = cost + liter * price
        price = city[i]
        liter = 0
    if i == n-1:  # n-1인 경우의 road는 없으므로
        break
    liter += road[i]

print(cost)

# 현재 주유하는 도시 이후에 리터당 가격이 현재 도시보다 저렴한 도시가 있는지
# 있으면 해당 도시에 도달하기까지 필요한 만큼 주유
# 없으면 끝까지 도달할 수 있을만큼 주유

