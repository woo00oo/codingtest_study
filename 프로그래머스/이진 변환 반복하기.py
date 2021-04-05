# 10 -> 2진수 변환 format(10진수,'b')
# 10 -> 8진수 변환 format(10진수,'o')
# 10 -> 16진수 변환 format(16진수,'x')

def solution(s):
    cnt, cnt_0 = 0, 0

    while s != '1':
        s = list(s)
        removed = 0
        for i in range(len(s)):
            i -= removed
            if s[i] == '0':
                del s[i]
                removed += 1
                cnt_0 += 1
        s = str(format(len(s), 'b'))
        cnt += 1
    answer = [cnt, cnt_0]

    return answer


