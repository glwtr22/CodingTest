N = int(input())
num = []
for i in range(N):
    x = int(input())
    if x == 0:
        num.pop()
    else:
        num.append(x)

print(sum(num))