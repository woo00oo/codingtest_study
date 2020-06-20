def solution(participant, completion):
    participant.sort()
    completion.sort()
    for name1,name2 in zip(participant,completion):
        if name1 != name2 :
            return name1
    return participant[-1]




participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
result = solution(participant,completion)

print(result)