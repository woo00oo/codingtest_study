# 문자열 정렬 : 문자열 -> 리스트로 변환 -> 리스트 정렬 -> 리스트를 문자열로 다시 변환 join 메소드 활용

def solution(s):
    answer = list(s)
    answer.sort(reverse=True)
    answer = ''.join(answer)
    return answer