n = int(input())
num = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

num.sort()

# 재귀 활용한 이진 탐색
def search(num, t, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if num[mid] == t:
        return 1
    elif num[mid] > t:
        return search(num, t, start, mid-1)  # return 유무
    else:
        return search(num, t, mid+1, end)

for t in find:
    print(search(num, t, 0, n-1))