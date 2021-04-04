# 시간 초과, 범위의 모든 소수를 구할때는 효율적인 방법이 아님.
# def solution(n):
#     answer = 0
#     for i in range(2, n+1):
#         sosu = True
#         for j in range(2, i):
#             if i % j == 0:
#                 sosu = False
#         if sosu:
#             answer += 1
#     return answer

# 에라토스테네스의 체 방식으로 풀이.
# 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법.
# 1. 1은 제거 소수 아님 -> 2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고 나머지 2의 배수는 모두 지움 -> 3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수는 모두 지움
# 4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고 나머지 5의 배수를 모두 지움 -> 이렇게 반복해 나가며 1 ~ N 까지 범위의 소수를 판별.

def solution(n):
    cnt = [True]*(n+1)
    answer = 0

    for i in range(2, int(n**0.5)+1): # n 의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사.
        if cnt[i]: # 만약 소수면
            for j in range(i+i, n+1, i):
                cnt[j] = False # 소수의 배수는 소수가 아님


    for i in range(2, n+1): # 소수 개수 카운트
        if cnt[i]:
            answer += 1
    return answer

print(solution(10))