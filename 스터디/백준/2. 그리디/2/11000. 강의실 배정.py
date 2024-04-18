from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
cl = []
for i in range(n):
    cl.append(tuple(map(int, sys.stdin.readline().split())))
cl.sort()

# 수업 시작 시간이 어떤 수업의 종료시간보다 같거나 늦으면 그 수업의 강의실에서 이어서 수업이 가능하다는 점
heap = [cl[0][1]] # 시작 시간이 가장 빠른 수업의 끝나는 시간
for s, t in cl[1:]:
    if heap[0] <= s:
        heappop(heap)
    heappush(heap, t)
print(len(heap))

'''
단순 구현, 그리디, 완전 탐색(백트래킹, DFS/BFS), DP !!! (시간 복잡도 생각하기), 이분 탐색, 
'''






# import sys
#
# n = int(input())
# cl = []
# for i in range(n):
#     cl.append(tuple(map(int, sys.stdin.readline().split())))
#
# cl.sort(key = lambda x : (x[1], x[0]))
#
# check = [0 for i in range(n)]
# total = 0
# cnt = 0
#
# while total != n:
#     idx = check.index(0)
#     endTime = cl[idx][1]
#     for i in range(1, n):
#         if cl[i][0] >= endTime and check[i] == 0:
#             endTime = cl[i][1]
#             check[i] = 1
#             total += 1
#     cnt += 1
#
# print(cnt)
