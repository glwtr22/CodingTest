# 1. 기본 연산
a, b = 'Hello', 'World'
print(a+b)
print(a*3)

# 2. 문자열 변환
a, b, c = 'hello', 123, True
print(type(a), type(b), type(c))
print(type(str(a)), type(str(b)), type(str(c)))

# 3. 인덱싱 / 슬라이싱
a = 'abcd efg'
print(a[0], a[1], a[2], a[-1], a[-2])
print(a[1:6])
print(a[-3:-1]) # -3 ~ -2
print(a[:])  # 전체
print(a[3:]) # 3 ~
print(a[:3]) # ~ 2

# 4. 문자열 복사 : =, str, [:]
a = 'abcdefg'

# 이하 방식은 두 변수의 메모리 주소가 동일함

# 1)
b = a
print(id(a), id(b))
print(b is a)

# 2)
c = str(a)
print(id(a), id(c))
print(c is a)

# 3)
d = a[:]
print(id(a), id(d))
print(d is a)