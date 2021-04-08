def solution(n):
    numbers = list(str(n))
    numbers.sort(reverse=True)
    answer = ''.join(numbers)
    return int(answer)
