# min() 함수를 이용하는 답안
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_v = min(data)
    result = max(result, min_v)

print(result)


# 2중 반복문 구조를 이용하는 답안
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_v = 10001
    for a in data:
        min_v = min(a, min_v)
    result = max(min_v, result)

print(result)