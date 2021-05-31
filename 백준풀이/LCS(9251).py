s1 = input()
s2 = input()
dp = [[0] * (len(s2) + 1) for _ in range(len(s1)+1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        # 가장 최근에 추가된 글자가 서로 같을때
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 # 두 글자가 추가되기 전 가장 큰 길이 + 1이 됨.
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 기존에 주어진 문자열로 만들 수 있던 최대 길이가 됨.

print(dp[-1][-1])