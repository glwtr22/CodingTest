import sys

n = int(input())
k = int(input())
point = list(map(int, sys.stdin.readline().split()))
point.sort()

answer = 0

wid = []
for i in range(1, len(point)):
    wid.append(point[i] - point[i-1])
wid.sort()
for i in range(k - 1):
    if len(wid) != 0:
        wid.pop()
answer = sum(wid)

print(answer)