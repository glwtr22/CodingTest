# 정렬하려는 리스트의 모든 원소 값이 0보다 크거가 같은 정수라 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)      # 리스트의 요소를 모두 포함할 수 있는 리스트 선언 및 0으로 초기화
                                    # (0 ~ max 값인 9, 총 10개의 숫자를 모두 포함할 수 있게 크기 10인 리스트 선언)
for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')