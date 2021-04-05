# upper() => 대문자 변환, lower() => 소문자 변환

def solution(s):
    li = list(s.split())
    for i in range(len(li)):
        li[i] = list(li[i])
        for j in range(len(li[i])):
            if j % 2 == 0:
                li[i][j] = li[i][j].upper()
            else:
                li[i][j] = li[i][j].lower()

    for i in range(len(li)):
        li[i] = ''.join(li[i])

    return ' '.join(li)


def solution2(s):
    li = s.split(' ')
    for i in range(len(li)):
        s_li = list(li[i])
        for j in range(len(s_li)):
            if j % 2 == 0:
                s_li[j] = s_li[j].upper()
            else:
                s_li[j] = s_li[j].lower()
        li[i] = ''.join(s_li)

    return ' '.join(li)


