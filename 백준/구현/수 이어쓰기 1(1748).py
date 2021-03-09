# 문제풀이:
#   N자리 수의 숫자를 입력 받았을 때, n-1 자리수까지의 총자리 수를 더하고, n자리수의 숫자들은 따로 계산한다.

N = input()
N_len = len(N) - 1
answer = 0
i = 0
while i < N_len:
    answer += 9 * (10 ** i) * (i + 1)
    i += 1
answer += ((int(N) - (10 ** N_len)) + 1) * (N_len + 1)

print(answer)