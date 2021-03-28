# combinations(조합) 을 활용하여 간단하게 풀이 가능
# 순열 ==> permutations를 활용

from itertools import combinations

def solution(numbers):
    answer = list()
    li = list(combinations(numbers,2))

    for i in li:
        if sum(i) not in answer:
            answer.append(sum(i))
    answer.sort()

    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))