# 괄호 짝 맞추기나, 이 문제처럼 서로 짝을 맞춰야하는 유형은 스택 자료구조를 사용하자.

N = int(input())
answer = 0

for _ in range(N):
    S = input()
    stack = []

    for i in range(len(S)):
        if len(stack) == 0:
            stack.append(S[i])
        elif stack[-1] == S[i]:
            stack.pop()
        else:
            stack.append(S[i])

    if not stack:
        answer += 1

print(answer)