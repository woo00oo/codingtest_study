arr = [['-' for _ in range(15)] for _ in range(5)]
answer = ''

for i in range(5):
    S = input()
    for j in range(len(S)):
        arr[i][j] = S[j]

for j in range(15):
    for i in range(5):
        if arr[i][j] != '-':
            answer += arr[i][j]

print(answer)