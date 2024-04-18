n = int(input())
num = list(map(int, input().split()))

if n == 1:
    num.sort()
    num.pop()
    print(sum(num))
    exit(0)

case = []
case.append((num[0], num[1], num[2]))
case.append((num[0], num[2], num[4]))
case.append((num[0], num[3], num[4]))
case.append((num[0], num[1], num[3]))
case.append((num[1], num[2], num[5]))
case.append((num[2], num[4], num[5]))
case.append((num[3], num[4], num[5]))
case.append((num[1], num[3], num[5]))

minSum = sum(case[0])
idx = 0
for i in range(1, len(case)):
    if sum(case[i]) < minSum:
        minSum = sum(case[i])
        idx = i

tmp = []
for c in case[idx]:
    tmp.append(c)

tmp.sort()
one = tmp[0]
two = one + tmp[1]
three = two + tmp[2]

top = three * 4 + two * 8 * (n-2) + one * 5 * (n-2) ** 2
bottom = two * 4 + one * 4 * (n-2)
print(top + bottom)