n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
d = [10001] * (m+1)  # 0원 ~ m원까지 각각의 금액에 대한 최소한의 화폐 개수를 구하는 방식

# 다이나믹 플밍, 보텀업
d[0] = 0  # 0원 일 때는 0
for i in range(n):  # 각각의 화폐 단위
    for j in range(array[i], m + 1): # 각각의 금액
        if d[j-array[i]] != 10001:   # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])