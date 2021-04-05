# 자릿수 접근은 int -> str 로 형 변환 후 인덱스로 접근하면 쉽게 해결 가능

def solution(n):
    answer = 0
    numbers = str(n)

    for i in range(len(numbers)):
        answer += int(numbers[i])

    return answer