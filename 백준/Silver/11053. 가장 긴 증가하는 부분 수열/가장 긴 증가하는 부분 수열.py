n = int(input())
num = list(map(int, input().split()))
dp = [1] * n    # 수열의 각 숫자들은 자기 자신 자체만으로 길이가 1인 증가부분수열

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)    # dp[i]에는 num[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이가 저장된다
            
print(max(dp))

'''
수열의 가장 긴 증가하는 수열의 길이 출력하기
'''