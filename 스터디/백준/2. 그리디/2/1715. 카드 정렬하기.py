from heapq import heappush, heappop
import sys

card = []

n = int(input())
for _ in range(n):
    heappush(card, int(sys.stdin.readline()))

total = 0
while len(card)>1:
    first = heappop(card)
    second = heappop(card)
    sum = first + second
    heappush(card, sum)
    total += sum
print(total)






import sys

n = int(sys.stdin.readline())

card = []
for _ in range(n):
    card.append(int(sys.stdin.readline()))

card.sort()

total = 0
while True:
    if len(card) == 1:
        break
    total = total + (card[0] + card[1])
    card[0] = total
    del card[1]

print(total)