def solution(scores):
    answer = ''
    avg_list = []

    for i in range(len(scores)):
        homework_score = []

        for j in range(len(scores[i])):
            homework_score.append(scores[j][i])

        min_score = min(homework_score)
        max_score = max(homework_score)

        # 유일 최저점인 경우
        if min_score == scores[i][i] and homework_score.count(min_score) == 1:
            homework_score.remove(min_score)

        # 유일 최고점인 경우
        if max_score == scores[i][i] and homework_score.count(max_score) == 1:
            homework_score.remove(max_score)

        avg_list.append(sum(homework_score) // len(homework_score))

    for avg in avg_list:
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer