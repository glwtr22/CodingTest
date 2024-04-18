n = 1260
count = 0

# 큰 화폐 단위부터 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
