# X, Y, Z로 Y기준 좌측의 합, 우측의 합을 구하여 최종적으로 둘 다 더 했을 때, 최대 값을 return

def solution(A):

    left_sum = [0] * len(A)
    right_sum = [0] * len(A)

    for i in range(1, len(A)-2):
        if left_sum[i-1] + A[i] > 0:
            left_sum[i] = left_sum[i-1] + A[i]

    for i in range(len(A)-2, 1, -1):
        if right_sum[i+1]+A[i] > 0:
            right_sum[i] = right_sum[i+1]+A[i]

    max_sum = 0

    for i in range(1, len(A)-1):
        if left_sum[i-1] + right_sum[i+1] > max_sum:
            max_sum = left_sum[i-1] + right_sum[i+1]

    return max_sum




