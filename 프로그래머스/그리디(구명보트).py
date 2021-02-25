def solution(people, limit):
    people.sort()
    p1, p2 = 0, len(people) - 1
    answer = 0

    while p1 <= p2:
        if people[p1] + people[p2] > limit:
            p2 -= 1
            answer += 1
        else:
            answer += 1
            p1 += 1
            p2 -= 1

    return answer