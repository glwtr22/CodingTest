# print(5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4)
from itertools import permutations

n = int(input())
sign = list(map(str, input().split()))

ans = []
for c in list(permutations(range(10), n+1)):
    for i in range(len(sign)):
        if sign[i] == '<':  # 만족 하지 않는 경우 쳐내기
            if c[i] > c[i+1]:
                break
        else:
            if c[i] < c[i+1]:
                break
    else:  # 앞의 for 문에서 break 되지 않은 경우에만 실행  (for-else와 while-els)
        ans.append(c)
ans.sort()
print(ans)
print(''.join(map(str, ans[-1])))
print(''.join(map(str, ans[0])))

# https://thought-process-ing.tistory.com/100
# https://wikidocs.net/190098

# 유석님 풀이
#
k = int(input())
arr = list(input().split())
def check(i,j,k):
    if k == '<':
        return i < j
    else:
        return i > j

def dfs(depth, s):
    global _max, _min

    if depth == k+1:
        if len(_min) == 0:
            _min = s
        else:
            _max = s
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), arr[depth-1]):
                visited[i] = True
                dfs(depth+1, s+str(i))
                visited[i] = False

_max = ''
_min = ''

visited = [False] * 10

dfs(0, '')

print(_max)
print(_min)