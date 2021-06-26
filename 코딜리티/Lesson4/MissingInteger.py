def solution(A):
    numbers = set(A)
    answer = 0

    for num in range(1, 1000001):
        if num in numbers:
            answer = num
        else:
            return answer + 1
