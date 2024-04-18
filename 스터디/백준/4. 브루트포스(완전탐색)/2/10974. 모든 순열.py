from itertools import permutations

n = int(input())
arr = [i for i in range(1, n+1)]
per = list(permutations(arr, n))

for p in per:
    print(*p)


# 백트래킹 풀이
n = int(input())
temp = []

def backtracking():
    if len(temp) == n:
        print(*temp)
        return
    for i in range(1, n+1):
        if i not in temp:
            temp.append(i)
            backtracking()
            temp.pop()

backtracking()