k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

start, end = 1, max(lan)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in lan:
        cnt += l//mid

    if cnt >= n: # 랜선 길이를 늘려야 함
        start = mid + 1  # if cnt == n 을 안 넣으면 더 비효율적인 거 아닌가 ?? 발견 즉시 탈출 가능한데 -> 밑의 풀이가 왜 안되는지 ..
    else:
        end = mid - 1

print(end)


'''cnt == N 일 떄, mid 반환하는 코드'''

# k, n = map(int, input().split())
# lan = []
# for _ in range(k):
#     lan.append(int(input()))
#
# start, end = 1, max(lan)
# while start <= end:
#     mid = (start + end) // 2
#     cnt = 0
#     for l in lan:
#         cnt += l//mid
#
#     if cnt == n:
#         print(mid)
#         exit(0)
#
#     elif cnt > n: # 랜선 길이를 늘려야 함
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(end)



'''
처음에는
가장 작은 랜선의 길이를 초기 값으로 설정하고
점점 1씩 줄여나가면서
그 값으로 주어진 랜선들을 전부 나눠보고 몫을 더해서
만들어야 하는 랜선 개수를 충족하면 그 값을 정답으로 출력하려고 했다
'''