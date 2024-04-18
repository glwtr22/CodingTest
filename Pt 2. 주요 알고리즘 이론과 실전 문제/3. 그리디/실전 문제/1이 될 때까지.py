# 내 풀이
n, k = map(int, input().split())
result = 0

cnt = 0
while n != 1:
    if n % k == 0:
        cnt += 1
        n //= k
    else:
        cnt += 1
        n -= 1

print(cnt)


# 단순하게 푸는 풀이
n, m = map(int, input())
result = 0

while n >= k:
    while n % k != 0:   # N이 아주 커질 경우에도 빠르게 동작하게 하기 위해, N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 작성
        n-=1
        result += 1
    n//=k
    result += 1

print(result)


# 다른 풀이
n, k = map(int, input().split())
result = 0

while True:
    # N 이 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n-target)
    n = target

    if n<k:
        break

    result +=1
    n //= k

result += (n-1)
print(result)