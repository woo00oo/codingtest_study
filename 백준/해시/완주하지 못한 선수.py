# 문제 풀이:
#   동명이인이 있다면 , zip안에 있는 값이 다른 것이 있기 때문에 그 다른 것들 중 하나 가 답.
#   zip안에 짝지어진 값이 모두 같거나, 중복된 것이 맨 뒤에 정렬됐다면 길이가 하나 차이 나는 s의 마지막 값이 답이 됨.

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for name1,name2 in zip(participant,completion):
        if name1 != name2 :
            return name1
    return participant[-1]


