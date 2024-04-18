n = int(input())
array = [0] * 1000001

for i in list(map(int, input().split())):  # input().split() 를 바로 iterater 객체로 for문에서 사용
    array[i] = 1

m = int(input())
find = list(map(int, input().split()))

for f in find:
    if array[f] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
