array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:   # 재귀 함수 탈출 조건
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:  # 엇갈리지 않는 동안

        # left는 오른쪽, right는 왼쪽으로 이동하면서
        while left <= end and array[left] <= array[pivot]:  # pivot보다 큰 값 찾기
            left += 1
        while right > start and array[right] >= array[pivot]: # pivot보다 작은 값 찾기 (start는 피벗임으로 등호 X)
            right -= 1

        if left > right:    # 엇갈렸다면, 작은 데이터와 피벗을 교체
            array[right] , array[pivot] = array[pivot], array[right]
        else:               # 엇갈리지 않았다면, 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]

    # 엇갈린 경우에 분할된 리스트 각각에 대해서, quick_sort 실행 (right 인덱스가 분할 기준 !)
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array)-1)
print(array)