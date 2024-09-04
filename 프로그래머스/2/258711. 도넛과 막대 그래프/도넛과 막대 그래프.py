def solution(edges):
    # {노드 번호 : [나가는 간선, 들어오는 간선]}
    def count_edges(edges):
        edge_counts = {}
        for a, b in edges:
            if not edge_counts.get(a):
                edge_counts[a] = [0, 0]
            if not edge_counts.get(b):
                edge_counts[b] = [0, 0]
                
            edge_counts[a][0] += 1
            edge_counts[b][1] += 1
        
        return edge_counts
    
    def check_answer(edge_counts):
        answer = [0, 0, 0, 0]
        
        for key, counts in edge_counts.items():
            # 생성된 정점 저장
            if counts[0] >= 2 and counts[1] == 0:
                answer[0] = key
            # 막대 모양 그래프
            elif counts[0] == 0 and counts[1] > 0:
                answer[2] += 1
            # 8자 모양 그래프
            elif counts[0] >= 2 and counts[1] >= 2:
                answer[3] += 1
                
        # 도넛 모양 그래프 수
        answer[1] = (edge_counts[answer[0]][0] - answer[2] - answer[3])
        
        return answer
    
    edge_counts = count_edges(edges)
    answer = check_answer(edge_counts)
    
    return answer


'''
도넛 : n개 정점, n개 간선
막대 : n개 정점, n-1개 간선
8자모양 : 2n+1개 정점, 2n+2개의 간선 (도넛 모양 결합시킨 형태)

정점 하나와 각 그래프들의 임의의 정점 하나로 향하는 간선들을 연결 후, 정점들에 서로 다른 번호 매김
간선 정보가 주어질 때, 정점 생성 전 각 그래프들의 개수 구하기

반환값 : 생성한 정점 번호, 도넛 그래프 개수, 막대 그래프 개수, 8자 모양 그래프 개수
'''

'''
<각 그래프 혹은 정점이 갖는 특징>
- 생성된 정점 : 나가는 간선이 2개 이상 존재, 들어오는 간선은 0개
- 막대 모양 그래프 : 들어오는 간선이 없는 정점 하나, 나가는 간선이 없는 정점 하나
- 도넛 모양 그래프 : 모든 정점이 나가는 간선과 들어오는 간선 하나씩 존재
- 8자 모양 그래프 : 1개의 정점은 나가는 간선 2개, 들어오는 간선 2개 존재

<생성된 정점과 그래프 찾는 절차>
1. 들어오는 간선이 없고, 나가는 간선이 2개 이상인 생성된 정점 찾기
2. 생성된 정점과 연결된 간선 개수 = 그래프 총 개수 찾기
3. 생성된 정점과 연결된 간선 모두 삭제
4. 막대 모양 그래프 개수 구하기 (들어오는 간선 없는 정점 개수 혹은 나가는 간선 없는 정점 개수를 통해 구할 수 있음)
5. 8자 모양 그래프 개수 구하기 (들어오는 간선, 나가는 간선 개수 2개인 정점 개수로 구할 수 있음)
6. 도넛 모양 그래프 개수 구하기 (전체 그래프 개수에서 막대, 8자 그래프 개수 빼서 구할 수 있음)
'''