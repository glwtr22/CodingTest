# 한 번 계산된 결과를 메모이제이션(Memoization) 하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    # print('f{' + str(x) + '}', end = " ")
    # 재귀 함수 종료 조건
    if x == 1 or x == 2:
        return 1

    # 이미 계산된 적 있는 문제라면 저장된 값 반환
    if d[x] != 0:
        return d[x]

    # 계산된 적 없는 문제라면 피보나치 결과 저장 후 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(6))