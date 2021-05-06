S = input()
revers_word = []
tag = False
answer = ''
for idx in range(len(S)):
    if S[idx] == '<':
        if len(revers_word) != 0:
            revers_word.reverse()
            answer += ''.join(revers_word)
            revers_word.clear()
        tag = True
        answer += S[idx]
    elif S[idx].isalnum():
        if tag:
            answer += S[idx]
        else:
            revers_word.append(S[idx])
    elif S[idx] == ' ':
        if len(revers_word) != 0:
            revers_word.reverse()
            answer += ''.join(revers_word)
            revers_word.clear()
        answer += S[idx]

    elif S[idx] == '>':
        tag = False
        answer += S[idx]

    if idx == len(S) - 1:
        revers_word.reverse()
        answer += ''.join(revers_word)

print(answer)