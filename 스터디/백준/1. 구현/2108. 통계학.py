from collections import Counter
import sys

n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

# 1. 산술평균
print(round(sum(num)/n))

#2. 중앙값
print(num[len(num)//2])

#3. 최빈값
tmp = Counter(num).most_common(2) # 최빈값 상위 2개 출력
# print(tmp)
if len(tmp) > 1:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])

# 4. 범위
print(num[len(num)-1] - num[0])


# def find_most(most):
#     sum = 0
#     for i in range(0, most):
#         sum += cnt[i]
#     return num[sum]
#
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# num = []
# for i in range(n):
#     num.append(int(input()))
#
# num.sort()  # 오름차순 정렬
#
# mean = sum(num)/n
# mid = num[len(num)//2]
#
# # 최빈값 구하기  // Counter 활용?
#
# #정렬된 순서대로 빈도수 cnt 리스트에 저장
# cnt = []
# idx = 0
# while idx < len(num):
#     tmp = num.count(num[idx])
#     cnt.append(tmp)
#     idx = idx + tmp
#
# # 최대 빈도수 구하기
# max = cnt[0]
# flag = 0
# for i in range(1, len(cnt)):
#     if cnt[i] > max:
#         max = cnt[i]  # max : 최빈값의 빈도 수
#
# # most = cnt[cnt.index(max)]
# if len(cnt) == 1:
#     most = num[0]
# elif cnt.count(max) != 1:  # 최빈값이 하나일 때
#     most = cnt.index(max, cnt.index(max)+1)
#     most = find_most(most)
# else: # 최빈 값이 두 개 이상일 때
#     most = find_most(cnt.index(max))
#
# range = num[len(num)-1] - num[0]
#
# print(round(mean))
# print(mid)
# print(most)
# print(range)
#
#
# import sys
# from collections import Counter
#
# input = sys.stdin.readline
#
# N = int(input())
# num=[]
#
# for _ in range(N):
# num.append(int(input()))
#
# num = sorted(num)
# print(round(sum(num)/len(num))) #산술평균, sum으로 O(N)
#
# print(num[len(num)//2]) #중앙값 sorted로 O(NlogN)
#
# #최빈값 O(NlogN)
# cnt = Counter(num).most_common(2) # Counter는 O(N), most_common O(NlogN)
# if len(num) > 1:
#     if cnt[0][1] == cnt[1][1]:
#         print(cnt[1][0])
#     else:
#         print(cnt[0][0])
# else:
#     print(cnt[0][0])
#
# print(num[-1]-num[0]) #범위 O(1)


#Counter('hello world').most_common()
#[('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
