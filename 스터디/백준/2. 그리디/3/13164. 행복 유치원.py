n, k = map(int, input().split())
p = list(map(int, input().split()))

sub = []
for i in range(1, n):
    sub.append(p[i]-p[i-1])

sub.sort()
for _ in range(k-1):
    sub.pop()
print(sum(sub))