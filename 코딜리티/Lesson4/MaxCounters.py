# 효율성 실패 O(N*M)

def solution(N, A):
    answer = [0] * N
    max_num = 0
    for i in range(len(A)):
        if 1 <= A[i] <= N:
            answer[A[i]-1] += 1
            if answer[A[i]-1] > max_num:
                max_num = answer[A[i]-1]
        else:
            answer = [max_num] * N

    return answer

# O(N+M) 통과

def solution2(N, A):
    cnt_li = {i: 0 for i in range(1, N+1)}
    max_sum = 0
    max_num = 0

    for key in A:
        if key == N+1:
            max_sum += max_num
            cnt_li.clear()
            max_num = 0
        else:
            if key not in cnt_li:
                cnt_li[key] = 1
            else:
                cnt_li[key] += 1
            max_num = max(max_num, cnt_li[key])

    answer = [max_sum] * N

    for key, value in cnt_li.items():
        answer[key-1] += value

    return answer
