# 정답은 맞추긴 하였지만 더 간단하게 풀이할 수 있었다.

N = int(input())
li = [int(input()) for _ in range(N)]
li.sort(reverse=True)
answer = 0
sails = (N // 3) * 3
for i in range(0,sails,3):
    answer += li[i] + li[i+1]
reminders = N - sails
i = -1
while reminders > 0:
    answer += li[i]
    i -= 1
    reminders -= 1
print(answer)

# 다른 사람 풀이
N = int(input())
li = [int(input()) for _ in range(N)]
li.sort(reverse=True)
answer = 0
cnt = 1
for i in range(N):
    if cnt<3:
        answer += li[i]
        cnt += 1
    else:
        cnt = 1
print(answer)
