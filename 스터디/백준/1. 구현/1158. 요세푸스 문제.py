n, k = map(int, input().split())
li =[i+1 for i in range(n)]  # [1,2,3,4,5,6,7]
idx = k-1
answer = []
while li:
    answer.append(li[idx])
    del li[idx]
    idx += (k-1)
    if len(li) == 0:
        break
    idx %= len(li)

print("<" + ", ".join(map(str, answer)) + ">")

# print(str(answer).replace('[', '<').replace(']', '>'))