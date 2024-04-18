number ="4177252841"
k = 4

answer = str(number)
print(answer)
i=0
while i<len(answer)-1 and k>0 :
    if answer[i]< answer[i+1]:
        answer=answer[:i]+answer[i+1:]
        k=k-1
        if i>0:
            i=i-2
        else:
            i=i-1
    i=i+1


if k>0 :
    answer=answer[:len(answer)-k]

print(answer)

# 코드 실행은 되는데 정답은 아닌 코드

def solution(number, k):
    numbers = list(number)
    idxList = []

    # 앞에서부터 탐색
    # 현재 탐색하고 있는 숫자가, 그 다음 숫자보다 작을 경우에
    # 현재 탐색하고 있는 숫자 제거

    flag = 0
    for idx, n in enumerate(numbers):
        if k == 0:
            flag = 1
            break
        if idx != len(numbers) - 1:
            if numbers[idx] < numbers[idx + 1]:
                k -= 1
                idxList.append(idx)

    idxList.sort(reverse=True)
    for i in idxList:
        del numbers[i]
    if k > 0:
        numbers = numbers[:len(numbers)-k]

    answer = ''.join(numbers)

    return answer