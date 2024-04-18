from itertools import permutations

n = int(input())
num = list(map(int, input().split()))

per = permutations(num, n)

result = []
for p in per:
    eq = 0
    for i in range(len(p)-1):
        eq += abs(p[i] - p[i+1])
        result.append(eq)

print(max(result))




n = int(input())
a = list(map(int, input().split()))
t = []  # 백트래킹을 적용할 리스트

ans = 0
def dfs(depth):
    global n, ans
    if depth == n:
        total = 0
        for i in range(1, n):
            total += abs(t[i-1] - t[i])
        ans = max(ans, total)
        return

    for i in range(n):
        if a[i] not in t:
            t.append(a[i])
            dfs(depth + 1)
            t.pop()

dfs(0)
print(ans)