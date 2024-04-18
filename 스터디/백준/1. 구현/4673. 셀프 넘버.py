'''
양의 정수 n 에 대해서 n과 n의 각 자리 수를 더하는 함수 d(n)
무한 수열 생성 가능
n은 d(n)의 생성자
생성자가 한 개보다 많은 경우도 존재 > 101의 생성자는 91, 100
생성자 없는 숫자는 셀프 넘버
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하기
'''

# 처음 풀이, 시간 초과
def constructor(n):
    for num in range(1, n):
        sum = num
        while num > 0:
            x = num % 10
            sum += x
            num //= 10
        if sum == n:
            return True
    return False

for i in range(1,10000 + 1):
    if constructor(i) == False:
        print(i)

# 처음 풀이와 접근법은 같지만 str 함수를 활용한 풀이
def constructor(n):
    for i in range(1, n):
        st = str(i)
        total = sum(list(map(int, st))) + i
        if total == n:
            return True
    return False

for i in range(1,10000 + 1):
    if constructor(i) == False:
        print(i)

# 1~10000까지의 숫자를 하나씩 데리고 와서, 해당 숫자까지의 숫자들을 더해보면서 생성자의 유무를 확인
# 있으면  true, 없으면 false 출력  -> n 이 커질수록 n^2 의 시간복잡도를 갖게 된다.




numbers = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i): # 많아 봤자 해당 숫자의 자리수만큼을 더 돈다
        i += int(j)
    generated_num.add(i)

self_num = sorted(numbers - generated_num)
for num in self_num:
    print(num)