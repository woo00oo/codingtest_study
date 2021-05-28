# 첫번째 시도 : 실패
# 먼저 나온 수가 엄청 큰 수여서 뒤의 수를 append할 수 없는 경우
# ex) 1 10 2 3 4 의 경우

N = int(input())
A = list(map(int, input().split()))
number = 0
answer = []

for num in A:
    if number < num:
        answer.append(num)
        number = num

print(len(answer))

# -----------------------------
# dp 활용
# 첫번째 인덱스부터 수열의 길이의 최댓값을 저장해 나간다.
# ex) 수열 a = [10, 20, 10, 30, 20, 50]이 있을때,
# 4번째 숫자(30)까지의 수열의 길이의 최댓값은 첫번째 숫자부터 검사를 해 나가서 자기 자신(30)보다 작은 숫자들 중 가장 큰 길이를 구하고 그 길이에 +1을 하면 된다.


N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    for j in range(i):
        # 자기 자신보다 작은 숫자들 중에서 가장 큰 길이
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
