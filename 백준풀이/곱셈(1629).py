# 문제풀이 :
#   분할 정복 알고리즘.
#   시간 초과를 해결하기 위해서 곱셈의 개수를 줄이는 분할 정복이 필요한다.

# ex) A=10, B=11,C=12
# 1. b의 값이 짝수인지 홀수인지 파악.
# 2. b의 값이 짝수라면 10^10 ->(10^5)^2 형태로 바꿔준다.
# 3. b의 값이 홀수라면 10^10 ->(10^5)^2 *10 형태로 바꿔준다.

def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % C
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % C # b가 짝수인 경우
        else:
            return temp * temp * a % C # b가 홀수인 경우

A, B, C = map(int, input().split())
result = power(A, B)
print(result)
