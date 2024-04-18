n = int(input())

array = []
for i in range(n):
    input_data = input().split()  # 일단 리스트로 저장한 후에,
    array.append((input_data[0], int(input_data[1])))  # 각 요소에 인덱스로 접근해 튜플로 생성한 후, 다시 리스트에 append

array = sorted(array, key = lambda student : student[1])

for student in array:
    print(student[0], end =" ")