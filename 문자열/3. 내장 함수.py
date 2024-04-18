# 1. 길이
a = '123456789'
print(len(a))



# 2. 개수
a = 'aabbbccccc'
print(a.count('a'))



# 3. 찾기 : find, index, rfind
a = 'abcdefgabcdefg'

# 1) find
print(a.find('c'))  # 처음 등장한 위치 인덱스 반환
print(a.find('cde'))
print(a.find('c', 0, 5))  # 범위 설정
print(a.find('z'))  # 없으면 -1 반환
print(a.find('cee'))
print(a.find('c', 3, 5))
print(a.find('c', 7, 14))

# 2) index
print(a.index('c'))
print(a.index('cde'))
print(a.index('c', 0, 5))
# print(a.index('z'))
# print(a.index('cee'))
# print(a.index('c', 3, 5))

# find와 index 공통점 : 문자열 내에서 찾을 값이 처음 나타나는 위치를 탐색함
# 차이점 : 문자열 내 찾을 값이 없는 경우 find는 -1, index는 AttributeError 발생

# 3) rfind
print(a.rfind('c'))  # 오른쪽 끝부터 찾기



# 4. 구분자로 나누고(split) 합치기(join)

# 1) split : "문자열"을 구분자 기준으로 나눠 줌
a = 'ab,c d,e fgh'
print(a.split())
print(a.split(','))
print(a.split('e k'))

# 2) join : "문자열 또는 리스트"를 구분자로 합쳐 줌
a = 'ab cde'
print('/'.join(a))

a = ['a','b','c','d','e']
print(','.join(a))