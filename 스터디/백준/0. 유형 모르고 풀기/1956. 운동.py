# 9:27 ~
# [참고] : https://velog.io/@nkrang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1956-%EC%9A%B4%EB%8F%99-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 1. 플로이드 워셜 풀이
V, E = map(int, input().split())
matrix = [[int(1e9)] * (V+1) for _ in range(V + 1)]
for _ in range(E):
    x, y, c = map(int, input().split())
    matrix[x][y] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = 1e9
# 사이클인 경우들 중 최소값 찾기 (i-> i인 경우들 중 최소)
for i in range(1, V+1):
    answer = min(answer, matrix[i][i])

if answer == 1e9:
    print(-1)
else:
    print(answer)


# 2. 다익스트라 변형 풀이 -> 메모리 초과(코드만 이해)
import heapq as hq

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
dist = [[1e9] * (V+1) for _ in range(V+1)]

heap = []
for _ in range(E):
    x, y, c = map(int, input().split())
    graph[x].append([c, y])
    dist[x][y] = c
    # heap에 [비용, 출발지, 도착지] 3개 값을 넣기
    hq.heappush(heap, [c, x, y])

while heap:
    d, s, g = hq.heappop(heap)
    # 출발지와 도착지가 같으면 사이클
    # heap을 사용하기 때문에 처음 나온 사이클이 최소 비용 사이클임
    if s == g:
        print(d)
        break

    if dist[s][g] < d:
        continue

    for nd, ng in graph[g]:
        new_d = d + nd
        # s->g->ng로 가는게 이미 저장되어 있는 s->ng보다 빠르면 갱신
        if new_d < dist[s][ng]:
            dist[s][ng] = new_d
            hq.heappush(heap, [new_d, s, ng])

else:
    print(-1)


'''
방향성이 있는 그래프에서 최소 비용의 사이클 찾기 (불가능한 경우 -1)
'''

'''
v개 마을과 e개의 도로
도로는 일방통행
1번 부터 v번
운동을 하기 위한 경로 찾는데, 사이클을 찾기를 원한다
사이클을 이루는 도로의 길이 합이 최소가 되도록
두 마을을 왕복하는 것도 사이클에 포함
'''