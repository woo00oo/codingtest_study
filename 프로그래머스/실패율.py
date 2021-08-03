# 어떨 때 뒤에 것을 계산을 안해 시간 복잡도를 단축할 수 있을까 고민해 보자.

def solution(N, stages):
    dic = {}
    num = len(stages)

    for i in range(1, N+1):
        if num != 0:
            c = stages.count(i)
            dic[i] = c / num
            num -= c
        else: # 0명이 되면 그 이후 스테이지는 어차피 0임
            dic[i] = 0

    return sorted(dic, key=lambda x: dic[x], reverse=True)


'''
추가 정리:
    딕셔너리도 정렬이 된다.
    sorted(dict) => key를 오름차순으로 정렬한 key 리스트를 반환
    
    sorted(dict, key=lambda x:dict[x]) => value값을 기준으로 정렬한 key리스트를 반환(value가 같으면 key기준 정렬)



'''