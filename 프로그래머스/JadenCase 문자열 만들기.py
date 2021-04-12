# capitalize() -> 문자열의 첫 글자를 대문자로 변환해주는 함수(첫 번째 문자가 이미 대문자이면 아무 작업도 수행하지 않음)

def solution(s):
    li = s.split(' ')
    for i in range(len(li)):
        li[i] = li[i].capitalize()
    answer = ' '.join(li)
    return answer