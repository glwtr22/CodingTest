def binary_search(array, target, start, end):
    # 시작 점이 끝 점보다 큰 경우에 대한 처리
    if start > end:
        return None
    mid = (start + end) // 2

    # target 단어를 찾은 경우 반환
    if array[mid] == target:
        return mid

    # 그 이외의 경우에 대해서는 재귀 처리
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# 입력 받기
n , target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)