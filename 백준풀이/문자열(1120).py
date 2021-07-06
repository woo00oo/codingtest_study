# 1차 시도

A, B = input().split()

answer = 1e9

while True:
    if len(A) == len(B):
        break

    # 앞에 추가 할 경우
    A1 = B[0] + A
    A1_di = len(B) - len(A1)
    for i, j in zip(A1, B):
        if i != j:
            A1_di += 1

    #뒤에 추가 할 경우
    A2 = A + B[-1]
    A2_di = len(B) - len(A2)
    for i, j in zip(A2, B):
        if i != j:
            A2_di += 1

    if A2_di > A1_di:
        A = A1
        if answer > A1_di:
            answer = A1_di
    else:
        A = A2
        if answer > A2_di:
            answer = A2_di

print(answer)

# 2차시도:


A, B = input().split()
answer = 1e9

for i in range(len(B)-len(A)+1):
    B1 = B[i:i+len(A)]
    di = 0
    for i, j in zip(A, B1):
        if i != j:
            di += 1
    if answer > di:
        answer = di

print(answer)