def solution(s):
    i = len(s) // 2
    if len(s) % 2 == 0:
        return s[i-1:i+1]
    else:
        return s[i]

