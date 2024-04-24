n = int(input())

def star(l):
    if l == 3:
        return ['***', '* *', '***']

    arr = star(l//3)  # l이 9일 때, arr에는 기본 3x3패턴이 들어있다
    stars = []

    for i in arr:  # 3x3 패턴의 각 행을 도는 반복문 : 가장 위의 1/3 조각
        stars.append(i*3)
    for i in arr: # 가운데 1/3 조각
        stars.append(i + ' ' * (l//3) + i)
    for i in arr:
        stars.append(i*3)

    return stars

# print(star(n))
print('\n'.join(star(n)))

'''
https://sujeng97.tistory.com/11
https://cotak.tistory.com/38
'''


# N = int(input())
# for i in range(N):
#     for j in range(N):
#         if (i - 1) % 3 == 0 and (j - 1) % 3 == 0:
#             print(' ', end='')
#         elif



# # N = 3인 경우
# for i in range(3):
#     for j in range(3):
#         if i == 1 and j == 1:
#             print(' ', end='')
#             continue
#         print('*', end='')
#     print()
#
#
#
#
# # N = 9인 경우
# def printBlank(size):
#     for i in range()
#
#
# for i in range(3):
#     for j in range(3):
#         if i == 1 and j == 1:
#             printBlank(9//3)