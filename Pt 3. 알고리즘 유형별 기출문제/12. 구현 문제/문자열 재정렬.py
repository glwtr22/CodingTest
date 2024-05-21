inStr = input()
alp = []
total = 0
for s in inStr:
    if 'A' <= s and s<='Z':
        alp.append(s)
    else:
        total += int(s)

alp.sort()
# K1KA5CB7
# AJKDLSI412K4JSJ9D
print(''.join(alp) + str(total))

'''
내장 함수 명 피해서 변수명 짓기
'''