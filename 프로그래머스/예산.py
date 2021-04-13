def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if budget - d[i] >= 0:
            answer += 1
            budget -= d[i]
        else:
            break

    return answer