def solution(n):
    str_n = str(n)
    answer = list(str_n[::-1])
    for i in range(len(answer)):
        answer[i] = int(answer[i])

    return answer

print(solution(10000000000))