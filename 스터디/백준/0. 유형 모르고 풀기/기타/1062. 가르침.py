from itertools import combinations

n, k = map(int, input().split())
words = [input()[4:-4] for _ in range(n)]  # words에는 앞 뒤 4글자 제외한 중간 단어 저장

learned = {'a', 'n', 't', 'i', 'c'}  # 배운 글자 learned에 집합 데이터로 저장

k -= len(learned)  # k에 더 배울 수 있는 단어 수 저장

if k < 0:
    print(0)
    exit(0)
elif k == 21: # 알파벳 전체를 배울 수 있는 경우 : 모든 단어를 읽을 수 있다
    print(n)
    exit(0)

letters = []  # 입력으로 들어온 단어들의 알파벳 저장
for i in range(26):
    if chr(i+97) not in learned:  # a 유니코드 : 97
        letters.append(chr(i+97))

res = 0
combs = combinations(letters, k)  # 아직 안 배운 단어들 중 k개 조합
for comb in combs:  #  comb : 각각의 조합 경우
    cnt = 0
    for word in words:
        for char in word:
            if char not in comb and char not in learned:  # 현재 조합 경우에도 없고, 배운 단어에도 없으면
                break
        else:  # 반복문을 break해서 탈춣한 게 아니면
            cnt += 1  # (?)

    res = max(cnt, res)

print(res)




# n, k = map(int, input().split())
# if k < 5:  # 기본 단어도 읽을 수 없는 경우
#     print(0)
#     exit(0)
#
# # 기본 단어는 읽을 수 있는 경우
# word = []
# for _ in range(n):
#     word.append(input().strip())
#
