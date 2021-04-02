# 쉬운 문제라도 모든 문제를 꼼꼼하게 읽고 실수 하지 않기!

def solution(a, b):
    answer = 0
    if a < b:

        for i in range(a,b+1):
            answer += i

        return answer

    elif a > b:

        for i in range(b,a+1):
            answer += i

        return answer

    else:
        return a

print(solution(3,3))