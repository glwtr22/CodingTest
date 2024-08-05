n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []

one = 0
two = 0
while one < n and two < m:
    if a[one] < b[two]:
        answer.append(a[one])
        one += 1
    else:
        answer.append(b[two])
        two += 1

if one < n:
    answer += a[one:]
if two < m:
    answer += b[two:]

print(*answer)