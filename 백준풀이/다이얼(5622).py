numbers_3 = {'A', 'B', 'C'}
numbers_4 = {'D', 'E', 'F'}
numbers_5 = {'G', 'H', 'I'}
numbers_6 = {'J', 'K', 'L'}
numbers_7 = {'M', 'N', 'O'}
numbers_8 = {'P', 'Q', 'R', 'S'}
numbers_9 = {'T', 'U', 'V'}

word = input()
answer = 0

for c in word:
    if c in numbers_3:
        answer += 3
    elif c in numbers_4:
        answer += 4
    elif c in numbers_5:
        answer += 5
    elif c in numbers_6:
        answer += 6
    elif c in numbers_7:
        answer += 7
    elif c in numbers_8:
        answer += 8
    elif c in numbers_9:
        answer += 9
    else:
        answer += 10

print(answer)


# ---
# 조금 더 간단하게 풀이

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
answer = 0

for c in word:
    for d in dial:
        if c in d:
            answer += dial.index(d)+3

print(answer)
