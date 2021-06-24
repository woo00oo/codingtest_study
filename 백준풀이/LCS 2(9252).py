# 첫번째 풀이 :
#   LCS를 어떤식으로 저장해 나갈까를 고민해봤지만 dp 안에 값을 LCS의 길이를 구해나가는게 아니라 LCS 문자 자체를 저장해나가면서 풀어가면 된다.

sequence1 = input()
sequence2 = input()

dp = [[0] * (len(sequence2) + 1) for _ in range(len(sequence1) + 1)]
LCS = ''

for i in range(1, len(sequence2) + 1):
    for j in range(1, len(sequence1) + 1):
        if sequence2[i-1] == sequence1[j-1]:
            LCS += sequence2[i-1]
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

len_LCS = dp[-1][-1]
if len_LCS:
    print(len_LCS)
    print(LCS)
else:
    print(0)


# --------------
s1 = [0] + list(input().strip())
s2 = [0] + list(input().strip())
len_s1 = len(s1)
len_s2 = len(s2)
dp = [[""] * len_s2 for i in range(len_s1)]
for i in range(1, len_s1):
    for j in range(1, len_s2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + s1[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[len_s1 - 1][len_s2 - 1]))
print(dp[len_s1 - 1][len_s2 - 1])