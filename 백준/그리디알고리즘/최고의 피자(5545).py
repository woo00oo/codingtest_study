# 문제를 꼼꼼하게 읽자
# 토핑을 하나도 안올릴수도 있다. 무조건 토핑을 하나 올린다고 가정하에 그리디로 접근하여 시간을 좀 더 잡아 먹었다.

N = int(input())
A, B = map(int, input().split())
C = int(input())
K = [int(input()) for _ in range(N)]
K.sort(reverse=True)
Sum = C
answer = Sum // A
for i in range(N):
    Sum += K[i]
    Max = Sum // (A + B * (i+1))

    if Max > answer:
        answer = Max

print(answer)