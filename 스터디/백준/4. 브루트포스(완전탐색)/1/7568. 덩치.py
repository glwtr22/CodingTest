n = int(input())
p = []
for _ in range(n):
    p.append(tuple(map(int, input().split())))

result = []
for i in range(n):
    count = 0
    for j in range(n):
        if i != j:
            if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
                count += 1

    result.append(count)

for i in range(n):
    print(result[i] + 1, end=' ')