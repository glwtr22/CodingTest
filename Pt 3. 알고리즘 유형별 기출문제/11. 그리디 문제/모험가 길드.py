N = int(input())
tr = list(map(int, input().split()))

# 여행을 떠날 수 있는 그룹의 수 최댓값
# 그룹을 만들지 못해 남는 사람이 있어도 된다 **

tr.sort()

result = 0
count = 0

for t in tr:
    count += 1   # 먼저 카운팅 늘려주고 확인
    if count >= t:
        result += 1
        count = 0

print(result)

'''
그 아이디어가 맞는 아이디어인지부터 의심해
'''