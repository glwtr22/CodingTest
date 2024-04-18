from itertools import combinations

n, s = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    com = list(combinations(seq, i))
    for j in range(len(com)):
        S = sum(com[j])
        if S == s:
            cnt += 1

print(cnt)


import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

def subset_sum(idx, sub_sum):
    global cnt

    if idx >= n:
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1

    subset_sum(idx+1, sub_sum)
    subset_sum(idx+1, sub_sum - arr[idx])

subset_sum(0,0)
print(cnt)