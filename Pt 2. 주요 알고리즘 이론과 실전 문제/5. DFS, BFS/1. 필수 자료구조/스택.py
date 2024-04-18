stack = []

# 5, 2, 3, 7 삽입 > 삭제 > 1, 4, 삽입 > 삭제

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()     # pop() 함수 : 리스트의 맨 마지막 원소를 리턴하고 해당 원소를 삭제한다.
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])  # 최상단 원소부터 출력