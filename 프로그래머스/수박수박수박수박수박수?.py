def solution(n):
    answer = '수박'
    if n % 2 == 0:
        return answer * (n // 2)
    else:
        return answer * (n // 2) + '수'

