n = int(input())
cnt = 0
while True:
    if n < 0:       # N을 만들 수 없는 경우
        cnt = -1
        break
    if n % 5 == 0:
        cnt5 = n // 5
        cnt += cnt5
        break
    n -= 3
    cnt += 1
    if n == 0:
        break

print(cnt)