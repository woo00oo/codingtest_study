def solution(dartResult):
    score = [0, 0, 0]
    idx = -1

    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if i != 0 and dartResult[i-1].isdigit():
                continue
            idx += 1
            if dartResult[i+1] == '0':
                score[idx] = int(dartResult[i] + '0')
                continue

            score[idx] = int(dartResult[i])
        elif dartResult[i].isalpha():
            if dartResult[i] == 'D':
                score[idx] **= 2
            elif dartResult[i] == 'T':
                score[idx] **= 3
        else:
            if dartResult[i] == '*':
                if idx == 0:
                    score[idx] *= 2
                else:
                    score[idx-1] *= 2
                    score[idx] *= 2
            else:
                score[idx] = score[idx] * -1

    return sum(score)

