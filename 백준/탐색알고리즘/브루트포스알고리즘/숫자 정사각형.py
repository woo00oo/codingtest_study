import sys
N, M = map(int,input().split())
num_list = list()
for _ in range(N):
    num_list.append(list(sys.stdin.readline().strip()))

i = 1
answer = 0
while i <= N and i <= M:

    for row in range(N - (i-1)):
        for col in range(M - (i-1)):
            window = [one_row[col:col+i] for one_row in num_list[row:row+i]]
            if window[0][0] == window[0][-1] == window[-1][0] == window[-1][-1]:
                answer = max(answer, i*i)

    i += 1

print(answer)

