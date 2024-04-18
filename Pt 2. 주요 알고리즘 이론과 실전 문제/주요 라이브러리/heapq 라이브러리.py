# heapq로 힙 정렬 구현
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)

    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# heapq로 최대 힙을 구현해 내림차순 힙 정렬 구현
import heapq
def heapsort2(iterable):
    h2 = []
    result2 = []
    for value in iterable:
        heapq.heappush(h2, -value)

    for _ in range(len(h2)):
        result2.append(-heapq.heappop(h2))
    return result2

result2 = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result2)