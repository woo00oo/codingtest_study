def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1






clothes = [['yellow_hat','headgear'],['blue_sunglasses','eyewear'],
         ['green_turban','eyewear'],['green_turban','face']]


#print(solution(clothes))
