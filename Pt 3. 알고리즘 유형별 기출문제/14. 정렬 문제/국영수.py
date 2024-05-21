n = int(input())
student = []
for _ in range(n):
    name, k, e, m = input().split()
    student.append([name, int(k), int(e), int(m)])

student.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))  # 여러 개의 요소로 정렬 시 튜플, - 부호 사용

for s in student:
    print(s[0])