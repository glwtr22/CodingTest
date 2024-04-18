input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])- ord('a') + 1)  #ord() : 아스키코드 변환 함수

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (-1, 2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)