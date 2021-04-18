def solution(p, s):
    answer = 0
    p_index = 0
    s = list(s)
    for i in range(len(s)):
        i -= answer

        if s[i] != p[p_index % len(p)]:
            answer += 1
            del s[i]
        else:
            p_index += 1

    if ''.join(s[:len(p)]) != p:
        return -1
    else:
        answer += len(s) % len(p)
        return answer