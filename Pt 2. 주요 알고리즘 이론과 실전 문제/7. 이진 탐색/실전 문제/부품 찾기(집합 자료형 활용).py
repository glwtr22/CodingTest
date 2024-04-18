n = int(input())

array = set(map(int, input().split()))  # map 함수를 set 함수로 감싸면 set 자료형으로 반환할 수 있다.

m = int(input())
find = list(map(int, input().split()))

for f in find:
    if f in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

print(array)