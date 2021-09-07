def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p1, p2 in zip(participant, completion):
        if p1 != p2:
            return p1

    return participant[-1]