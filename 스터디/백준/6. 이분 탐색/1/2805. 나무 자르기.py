N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    log = 0
    for i in tree:
        if i >= mid:
            log += i - mid

    if log >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# start와 end가 같아지는게 왜 조건을 맍고한느 최대 나무 절단 높이를 찾은 시점인지 ???