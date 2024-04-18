def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else :
            start = mid + 1
    return None

N = int(input())
array = list(map(int, input().split()))  # map가 있고 없고의 차이
array.sort()
M = int(input())
find = list(map(int, input().split()))

for i in find:
    result = binary_search(array, i, 0, N - 1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')