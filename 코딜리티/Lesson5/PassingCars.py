# 동쪽으로 향해가는 차들이 서쪽으로 가는 차량을 몇 번 마주치게 되는지 총합을 출력.

def solution(A):
    answer = 0
    prefix_sum = [0, 0] # [0의 갯수, 1의 갯수]
    for car in A:
        if car == 0:
            prefix_sum[0] += 1
            prefix_sum[1] = 0
        elif car == 1:
            prefix_sum[1] = 1
            answer += prefix_sum[0] * prefix_sum[1]

    if answer > 1000000000:
        answer = -1

    return answer