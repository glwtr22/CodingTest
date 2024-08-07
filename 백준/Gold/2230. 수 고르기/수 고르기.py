import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

end = 1
ans = int(2e9)
for i in range(n):
    while arr[end] - arr[i] < m and end < n-1:
        end += 1
    if arr[end] - arr[i] >= m:
        ans = min(ans, arr[end] - arr[i])

print(ans)

'''
n개의 정수 수열
두 수를 골랐을 때(같은 수 가능), 그 차이가 M 이상이면서 제일 작은 경우?
'''