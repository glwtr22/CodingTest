N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  #   +,  -,  *,  / 의 개수가 순서대로 들어옴

maximum = -1e9
minimum = 1e9

def backtrack(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # 연산이 남아 있는지 확인 > 남은 연산 처리된 인자 값으로 재귀
    if plus:
        backtrack(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        backtrack(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        backtrack(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        backtrack(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


backtrack(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)