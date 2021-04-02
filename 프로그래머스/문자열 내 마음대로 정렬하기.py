# sort의 key 속성을 이용하여 간단하게 해결 가능.
# 람다 활용.
# 람다 다중 조건 => sort(key=lambda x : (x[0], -x[1])) -를 붙이면, 현재 정렬차순과 반대로.

def solution(strings, n):

    strings.sort(key=lambda x: (x[n], x))

    return strings

