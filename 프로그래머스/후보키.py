'''
새로 알게된 메소드

a.issubset(b) => a 집합이 b 집합의 교집합인지 알려주는 메소드

문제풀이 :
    1. 조합을 통해 후보키가 가능한 모든 인덱스를 구함
    2. 각 조합의 수 만큼 temp_li 배열에 튜플 값들을 넣어줌
    3. 유일성이 맞는지 확인(집합으로 변환 후의 길이와 일반 리스트의 길이가 같을 경우)
    4. 최소성이 맞는지 확인(issubset() 메소드를 통하여 부분집합이 있는지 체크)

'''

from itertools import combinations


def solution(relation):
    idx_li = [i for i in range(len(relation[0]))]
    answer = []

    for i in range(1, len(relation[0])+1):
        key_li = list(combinations(idx_li, i))

        for key in key_li:
            temp_li = [''] * len(relation)
            for num in key:
                for idx in range(len(relation)):
                    temp_li[idx] += relation[idx][num]

            set_temp_li = set(temp_li)
            if len(set_temp_li) == len(temp_li):
                check = True
                key = set(key)
                for ans in answer:
                    if ans.issubset(key):
                        check = False

                if check:
                    answer.append(key)

    return len(answer)


