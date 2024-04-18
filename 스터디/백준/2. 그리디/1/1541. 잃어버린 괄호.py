eq = input().split('-')

answer = 0
for i in eq[0].split('+'):
    answer += int(i)

for i in eq[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)


# 숫자는 0으로 시작 가능, 두 개 이상의 연산자가 연달아 나타날 수 없다

# 1. 숫자, 연산자 리스트로 각각 뽑아내기
# 2. 숫자 리스트의 인덱스 2개 조합으로 뽑기
# 3. 뽑은 인덱스에 해당되는 범위 수식 먼저 계산하고 전체 수식 계산해서 리스트에 저장
# 4. 리스트에 저장된 값들 중 최소 값 찾기


# from itertools import combinations
# eq = input() # 수식은 50보다 작거나 같음
# #1.
# num = []
# op = []
#
# st = 0
# end = 0
# for idx, e in enumerate(eq):
#     if e == '+' or e == '-':
#         op.append(e)
#         end = idx
#         num.append(int(eq[st:end]))
#         st = idx + 1
# num.append(int(eq[st:len(eq)]))
#
# print(num)
# print(op)
#
# #2.
# com = list(combinations(range(len(num)), 2))
# print(com)
# tmp = []
# for c in com:
#     print(c)
#     a, b = c
#     subeq = ""
#     for i in range(a, b+1):
#         subeq += str(num[i])
#         del num[i]
#         if i != b:
#             subeq += op[i]
#             del op[i]
#     num.insert(a, int(eval(subeq)))
#     equation = ''
#     for i in range(len(num)):
#         equation += str(num[i])
#         if i != (len(num) - 1):
#             equation += op[i]
#     tmp.append(int(eval(equation)))
#
# tmp.sort()
# print(tmp[0])