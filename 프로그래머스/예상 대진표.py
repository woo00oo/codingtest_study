# b가 짝수일 때 a + 1 == b 성립 즉 a와 b는 같은 라운드
# a = 4 , b = 5 a + 1 == b는 성립하지만 b가 홀수이기 때문에 a와 b는 같은 라운드에서 만난게 아님. 주의 !!

def solution(n,a,b):
    answer = 1
    if a > b:
        a, b = b, a

    while True:
        if a + 1 == b and b % 2 == 0:
            return answer

        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1

        a //= 2
        b //= 2
        answer += 1

print(solution(8,5,4))