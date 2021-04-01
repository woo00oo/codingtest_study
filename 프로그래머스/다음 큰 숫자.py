# format 메소드 활용
# 인자에 따라 10진수 -> 2진수, 8진수, 16진수로 변환 해주는 함수
# ex)
#  value = 60
#  b = format(value,'b') => 2진수
#  o = format(value,'o') => 8진수
#  h = format(value,'h') => 16진수
#  결과 타입은 str형 !!!


def solution(n):
    n2 = format(n,'b')

    while True:
        n += 1
        next_n = format(n,'b')

        if next_n.count('1') == n2.count('1'):
            return n


print(solution(78))
