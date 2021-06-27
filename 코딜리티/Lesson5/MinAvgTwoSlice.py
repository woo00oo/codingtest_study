# O(N^2)으로는 효율성 통과 x
# 이 문제를 해결하려면 수학적 규칙을 찾아야 한다. => subarray의 개념에 대해 알아야 한다.
# subarray : 기존의 array에서 slicing하여 만드는게 가능.

# a <= b일때, a와 b의 평균은 a 이상이 된다. (a=b일때, a와 b의 평균은 a, 즉 두수가 같은 경우는 a 혹은 b가 된다.)
# 마찬가지로, (a+b) <= (c+d)일때, (a,b)와 (c,d)의 평균은 (a+b)이상이 된다.
# 결국, 원소가 4개(a,b,c,d)인 그룹은 (a,b)와 (c,d)를 나누었을 때, 각각의 평균의 작은 값 이상이 된다.
# -> 2개인 그룹이 작은 값이 되므로 4개의 그룹은 고려할 필요가 없다.

# 예외로 원소가 3개인 그룹에서 2개인 그룹과 1개인 그룹의 경우를 확인해야 하지만,
#  = > 문제에서 주어진 조건에 의하면 그룹의 원소는 최소 2개 이상이므로 2개와 3개인 그룹만 비교하면 된다.

def solution(A):
    minAvg = (A[0]+A[1]) / 2
    answer = 0

    for i in range(len(A)-1):
        avg = (A[i] + A[i+1]) / 2
        if minAvg > avg:
            minAvg = avg
            answer = i

    for i in range(len(A)-2):
        avg = (A[i]+A[i+1]+A[i+2]) / 3
        if minAvg > avg:
            minAvg = avg
            answer = i

    return answer
