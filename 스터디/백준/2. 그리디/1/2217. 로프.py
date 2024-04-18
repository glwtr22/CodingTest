# 모든 로프를 사용할 필요가 없다

import sys

n = int(sys.stdin.readline())
rope = []
for i in range(n):
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)

mlist = []
while rope:
    rlen = len(rope)
    last = rope.pop()
    mlist.append(last * rlen) # rope[i]*[i+1]

# print(max(mlist))
# 리스트 min max 의 시간복잡도 : O(N) / sort 의 시간복잡도 O(NlogN) **
mlist.sort()
print(mlist.pop())