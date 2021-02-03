#문제해결:
# s = abab일때
# abab, bab, ab, b의 순으로 조건이 맞는지 검사( 문자열 앞에서부터 하나씩 제거)
# bab의 경우 팰린드롬이기 때문에 원래 문자열에서 제외한 a를 기존 s에 추가해준다
# 추가해준 문자열의 길이가 이 문제에서의 정답.

s = input()

for i in range(len(s)):

    if s[i:] == s[i:][::-1]:
        print(len(s)+i)
        break