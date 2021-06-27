# 조건 중에 index 순서에서 P보다 Q는 항상 커야하기 때문에, 배열 A의 제일 처음 값을 min으로 잡고, 결과를 max로 잡는다.
# 그리고 for문을 하나씩 돌릴때마다, 현재 배열의 값과 min값을 비교해서 더 작은 값을 min으로 할당하고, 현재 값에 min값을 뺀 후 max값을 비교하여 할당.

def solution(A):
    # A가 0또는 1의 값을 가지는 경우
    if len(A) < 2:
        return 0

    min_price = A[0]
    answer = 0
    for a in A:
        profit = a - min_price
        if answer < profit:
            answer = profit
        if min_price > a:
            min_price = a

    return answer
