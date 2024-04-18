from itertools import combinations

l, c = map(int, input().split())
ch = list(map(str, input().split()))
ch.sort()  # 조합 사용 전에 정렬

per = list(combinations(ch, l))
for p in per:  # p는 가능한 한 가지 조합 경우
    cnt = 0
    cnt2 = 0
    for ele in p:
        if ele == 'a' or ele == 'e' or ele == 'i' or ele == 'o' or ele == 'u':
            cnt += 1
        if ele != 'a' and ele != 'e' and ele != 'i' and ele != 'o' and ele != 'u':
            cnt2 += 1

    if cnt > 0 and cnt2 > 1:
        for ele in p:
            print(ele, end='')
        print()