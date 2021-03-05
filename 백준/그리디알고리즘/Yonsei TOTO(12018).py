# 문제풀이는 빠르게 해결하였지만, 답을 출력하는 과정에서 시간을 잡아 먹었다.

n, m = map(int,input().split())
answer = list()
cnt = 0
for _ in range(n):
    P, L = map(int,input().split())
    li = sorted(list(map(int,input().split())),reverse=True)
    if P < L:
        answer.append(1)
    else:
        answer.append(li[L-1])
answer.sort()
for num in answer:
    m -= num
    if m >= 0:
        cnt += 1
    else:
        break
print(cnt)