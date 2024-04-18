n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))

def change(A, B):
    A_copy = A[:]
    press = 0
    for i in range(1, n):
        if A_copy[i-1] == B[i-1]:  # 직전이 같은 경우, 현재 위치 버튼 누르지 않기
            continue
        press += 1
        for j in range(i-1, i+2):
            if j < n:  # j가 범위 안에 있을 때에만
                A_copy[j] = 1 - A_copy[j]  # 전구 스위치 눌러줌

    if A_copy == B:
        return press
    else:
        return 1e9


# 첫번째 전구의 스위치를 누루지 않는 경우
res = change(bulb, target)

# 첫번쨰 전구의 스위치를 누르는 경우
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]

res = min(res, change(bulb, target) + 1)

if res != 1e9:
    print(res)
else:
    print(-1)




# n = int(input())
#
# now = input()
# tar = input()
#
# if n == 2:
#     if now.count('0') == 2:
#         if tar.count('0') == 1:
#             print(-1)
#             exit(0)
#         elif tar.count('0') == 2:
#             print(0)
#             exit(0)
#         elif tar.count('0') == 0:
#             print(1)
#             exit(0)
# # N이 3인 경우
# if n == 3:
#     if tar == '000'
#
# for n in now:
#     now.append(int(n))
# for t in tar:
#     tar.append(int(n))
#
# def change(x, now):
#     now[x-1] = not now[x-1]
#     now[x] = not now[x]
#     if x+1<n:
#         now[x+1] = not now[x+1]
#
# # N이 4 이상인 경우
# cnt = 0
# for i in range(n):
#     if now[i] != tar[i]:
#         if i + 1 < n:
#             change(i+1, now)
#             cnt += 1
#
# if now == tar:
#     print(cnt)
# else:
#     print(-1)