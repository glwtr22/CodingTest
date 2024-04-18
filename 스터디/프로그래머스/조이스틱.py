def solution(name):
    alp = 0     # 알파벳 이동 횟수
    cur = len(name) - 1     # 기본 커서 이동 횟수

    for i, al in enumerate(name):
        alp += min(ord(al) - ord('A'), ord('Z') - ord(al) + 1)

        # 연속된 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 아래 3가지 경우 중 최소 이동 값으로 갱신
        # 1. 이전 커서 이동 값 ( 초기값 - 이름의 길이 - 1 )
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        cur = min([cur, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
    return alp + cur

print(solution("JAN"))



# def solution(name):
#     answer = 0
#     for i in range(len(name)):
#         sub = ord(name[i]) - ord('A')
#         print(sub)
#         if sub <= 13:
#             answer += sub
#         else:
#             answer += (len(name) - ord(name[i]) + ord('A'))
#
#     return answer
#
# print(solution("JAZ"))