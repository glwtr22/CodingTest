N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr = sorted(arr, reverse=True)

for i in arr:               # for i in range(N):
    print(i, end =" ")      # print(arr[i], end=" ") 보다 심플하다 !