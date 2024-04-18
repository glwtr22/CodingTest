n = int(input())
d = [0] * (n + 1)  # d[i]에 저장되는 값은 i를 1로 만드는 최소 연산 횟수

# 상향식 풀이 : 제일 작은 인덱스의 수부터 목표하는 값으로 향하는 것
for i in range(2, n + 1):
    # if 문을 하지 않아도 밑의 조건문에서 최소값으로 교체되기 때문에 어짜피 셋  다 시도하는것과 같은 결과
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])

# https://jae04099.tistory.com/199

# n = int(input())
#
# count = 0
# while n>1:
#     if n%3 == 0:
#         n //= 3
#     elif n%2 == 0:
#         n //= 2
#     else:
#         n -= 1
#     count += 1
#
# print(count)
