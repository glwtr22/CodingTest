# n : 생성할 원소의 개수
# target : 찾으려는 단어
# array : 생성한 원소들이 담긴 배열

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

# 입력 받기
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))