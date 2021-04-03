# 다양한 방식으로 해결 가능
# s.isalpha(), s.isdigit() => 문자열이 문자인지 숫자인지 체크해주는 함수
# ex) s = 'abc'
# s.isalpha() => true 리턴
# ex) s = '12a'
# s.isalpha() => false 리턴
# s.isdigit() => false 리턴
# -> 모두 일치해야함 모두 문자열이거나 모두 숫자이거나

def solution(s):
    number = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(s)):
        if s[i] not in number:
            return False
    if len(s) == 4 or len(s) == 6:
        return True
    else:
        return False

def solution(s):
    try:
        int(s)
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False

    except:
        return False

print(solution('13f'))

