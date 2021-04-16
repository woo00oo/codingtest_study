# 문제풀이:
#   combinations(조합), Counter 모듈 사용
#   Counter 리스트나 문자열의 각 원소의 빈도수를 세줌.

# 1차 시도.
# orders에 있는 각 원소들을 모두 더해 문자열이 중복되지 않게 course 넘버 만큼 조합을 구해주려고 했음
# 그 조합 리스트로 orders에 각 원소에 속해 있는지 판별하려고 하였지만 원소가 2개 3개 4개 이므로 in 함수가 불가능 했음

# 다른 풀이.
# orders의 각 원소들을 course 넘버 만큼 조합을 구해줌
# orders의 각 원소들의 조합 리스트를 모두 더해 temp 라는 리스트에 저장
# 이 temp 리스트를 Counter 모듈을 사용
# 해당 counter에 아무 값도 없거나 ( 해당 주문 조합이 나온적이 없었거나), 최댓값이 1이면(해당 조합을 주문한 사람이 혼자라면 ) 패스
# 아닐 경우 answer 에 최대값(현재 갯수에 해당하는 메뉴 조합 중 가강 많이 주문되었던 것) max가 여러개 일 경우 다 넣어줌


from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi

        counter = Counter(temp)
        print(counter.values())
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])