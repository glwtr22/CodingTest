# 1. replace, upper, lower
a = 'a,b,c,d,e'
print(a.replace(',', '/'))
print(a.replace(',', '/', 2)) # 세 번째 인자는 변경 횟수

a = 'a,b,c,D,E'
print(a.upper())
print(a.lower())

print('ABC'.isupper())
print('abc'.islower())
print('aBC'.isupper())
print('aBC'.islower())


# 2. strip, lstrip, rstrip
a = '   abc   '
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = '***abc***'
print(a.strip('*'))
print(a.lstrip('*'))
print(a.rstrip('*'))

a = '12321421abc11153212321'
print(a.strip('123'))  # 인자로 받은 문자열에 들어있는 문자들로 구성된 연속된 문자열만 잘라냄
print(a.lstrip('123'))
print(a.rstrip('123'))


# 3. zfill, rjust, ljust, center
a = 'abc'
print(a.zfill(10))  # 지정된 정수가 될 때까지 왼쪽에 0 채우기
print(a.zfill(3))

print(a.rjust(10, '*'))  # 지정된 정수가 될 때까지 원하는 값 채우기
print(a.ljust(10, '*'))
print(a.center(10, '*'))

# [참고 자료]
# https://easyjwork.tistory.com/3