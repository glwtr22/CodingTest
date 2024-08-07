n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0

sum_ = arr[0]
# 수 범위 보고 적절한 최댓값으로 설정하기
ans = 100001

while True:
    if sum_ < s:
        end += 1
        if end == n:
            break
        sum_ += arr[end]
    else:
        sum_ -= arr[start]
        ans = min(ans, end-start + 1)
        start += 1
    # 가장 길이가 짧은 것을 구하는 문제라 가능한 모든 경우를 훑은 코드가 되는 것인지?

print(ans if ans != 100001 else 0)