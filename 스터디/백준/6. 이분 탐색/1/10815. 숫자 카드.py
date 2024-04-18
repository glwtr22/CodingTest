import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

num.sort()

# 반복문 활용한 이진 탐색
def search(num, t, start, end):
    while start <= end:
        mid = (start + end) // 2
        if num[mid] == t:
            return 1
        elif num[mid] > t:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for t in find:
    print(search(num, t, 0, n-1), end = ' ')

