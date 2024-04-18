# 순서를 생각하면, 순열
# 순서를 생각하지 않으면, 조합

# 순열, r 개의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수
from itertools import permutations

data = ['a', 'b', 'c']
result = list(permutations(data, 3))  # r = 3
print(result)   # [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


# 조합, r 개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우의 수
from itertools import combinations

result1 = list(combinations(data, 2))
print(result1)  # [('a', 'b'), ('a', 'c'), ('b', 'c')]


# 중복 허용 순열
from itertools import product

result2 = list(product(data, repeat=2))  # [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]
print(result2)


# 중복 허용 조합
from itertools import combinations_with_replacement

result3 = list(combinations_with_replacement(data, 2))
print(result3)   # ('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]