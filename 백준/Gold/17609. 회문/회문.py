n = int(input())

for _ in range(n):
    st = input()
    left, right = 0, len(st) - 1
    answer = 0

    while left <= right:
        if st[left] == st[right]:
            left += 1
            right -= 1
        else:
            # 왼쪽 문자를 제거한 경우 회문인지 확인
            if st[left + 1:right + 1] == st[left + 1:right + 1][::-1]:
                answer = 1
            # 오른쪽 문자를 제거한 경우 회문인지 확인
            elif st[left:right] == st[left:right][::-1]:
                answer = 1
            else:
                answer = 2
            break

    print(answer)
