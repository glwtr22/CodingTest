import sys
n = int(sys.stdin.readline())

time = []
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time.append((s, e))

# 두번째 요소로 정렬 후, 두번째 요소가 동일한 경우에 대해서는 첫번째 요소로 정렬
time.sort(key = lambda x : (x[1], x[0]))

cnt = 1
endTime = time[0][1]
for i in range(1, n):
    if time[i][0] >= endTime:
        cnt += 1
        endTime = time[i][1]

print(cnt)