T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    imp = input().split()
    cnt = 0
    impt = []
    for idx, j in enumerate(imp):  # eunumerate는 항상 (idx, 값) 순으로 반환됨
        impt.append((j, idx))
    while impt:
        flag = 0
        for i in range(1, len(impt)):
            if impt[i][0] > impt[0][0]:
                impt.append((impt[0][0], impt[0][1]))  # pop(0) 인자가 있는 pop  /  waiting[0][1] == max(waiting, key=lambda x:x[1])[1]:
                del impt[0]
                flag += 1
                break
        if flag == 1:
            continue
        cnt += 1
        if impt[0][1] == m:
            print(cnt)
        del impt[0]