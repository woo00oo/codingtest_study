def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)):
        if len(phone_number) - i <= 4:
            answer += phone_number[i]
        else:
            answer += '*'

    return answer