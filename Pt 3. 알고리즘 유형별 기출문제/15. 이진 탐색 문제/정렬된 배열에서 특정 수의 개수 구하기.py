# 1. bisect 라이브러리 활용 풀이

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
num = list(map(int, input().split()))

left_idx = bisect_left(num, x)
right_idx = bisect_right(num, x)

cnt = right_idx - left_idx

if cnt != 0:
    print(cnt)
else:
    print(-1)



    
# 2. 이진 탐색 직접 구현 풀이

def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n-1)
    if a == None:
        return 0

    b = last(array, x, 0, n-1)

    return b - a + 1


def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    # 해당 target 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid + 1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 target 값을 가지는 원소 중에서 가장 오른쪽에 위치한 경우에만 인덱스 반환
    if (mid == n-1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)



n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)
