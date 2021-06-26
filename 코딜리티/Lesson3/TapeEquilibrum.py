# 효율성 실패 O(N^2)

def solution(A):
    answer = 1e9
    for i in range(1, len(A)):
        sum_number = abs(sum(A[:i]) - sum(A[i:]))

        if answer > sum_number:
            answer = sum_number

    return answer

# 시간복잡도 개선 O(N)
def solution2(A):
    total = sum(A)
    answer = 1e9
    left_sum_num = 0

    for i in range(len(A)-1):
        left_sum_num += A[i]
        right_sum_num = total - left_sum_num
        total_num = abs(left_sum_num-right_sum_num)

        if answer > total_num:
            answer = total_num

    return answer