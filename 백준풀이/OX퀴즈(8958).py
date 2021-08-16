T = int(input())

for _ in range(T):
    S = input()
    answer = 0
    score = 0
    for char in S:
        if char == 'O':
            score += 1
        else:
            score = 0

        answer += score

    print(answer)