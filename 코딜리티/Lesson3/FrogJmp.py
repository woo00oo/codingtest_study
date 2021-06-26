# 첫번째 풀이 : 효율성 실패
# 원인 : X,Y,D 범위가 1,000,000,000 이기에 O(N)으로는 풀 수 없다.

def solution(X, Y, D):
    now_location = X
    answer = 0

    while now_location < Y:
        now_location += D
        answer += 1

    return answer

# 두번째 풀이 : 통과 수학적 계산
# 항상 효율성을 생각하고 내가 작성한 코드의 시간복잡도로 해결이 가능한지 신중하게 생각하고 제출하자!

import math

def solution2(X, Y, D):
    return math.ceil((Y-X) / D)