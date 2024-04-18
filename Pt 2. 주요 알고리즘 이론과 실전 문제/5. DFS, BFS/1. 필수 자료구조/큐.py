from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# 5, 2, 3, 7 삽입 > 삭제 > 1, 4, 삽입 > 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()     # deque에는 리스트에 없는 popleft() 함수가 존재, 맨 왼쪽 데이터 반환 후 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

print(list(queue))  # deque 객체를 리스트 자료형으로 변환하려면 list() 함수 사용