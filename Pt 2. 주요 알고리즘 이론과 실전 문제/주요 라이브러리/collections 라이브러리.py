# collections의 deque 클래스 (리스트의 앞 뒤에 원소 삽입하기)
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)          # 맨 앞에 삽입 : appendleft,  맨 뒤에 삽입 : append

print(data)
print(list(data))  # 리스트로 반환 받고 싶으면, list 함수 이용


# collections의 Counter 클래스 (객체 내부의 원소 갯수 세기)
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

counter2 = Counter("hello world")
print(counter2)
print(dict(counter2))
print(list(counter2))

num = [3,3,3,2,2,1]
print(Counter(num).most_common(3))  # [(3, 3), (2, 2)]  3이 3번 , 2가 2번 ... most_common 함수의 인자로 들어간 숫자 만큼 알려줌 !