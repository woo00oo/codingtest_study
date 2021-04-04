# 문자열은 인덱스로 접근하여 인덱스 값을 바꿀 수 없음. replace 함수 등 활용

def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        # 대문자일경우
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        # 소문자일경우
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)