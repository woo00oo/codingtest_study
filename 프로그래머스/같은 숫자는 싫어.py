# 빈 배열을 하나 만들어 중복되지 않도록 서로 다른 숫자일 경우 append

def solution(arr):

    answer = [arr[0]]

    for i in range(len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])

    return answer

print(solution([1,1,3,3,0,1,1]))