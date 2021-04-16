# 아래 방법은 s의 원소가 한자리 수 일 경우만 가능함

def solution(s):
    li = []
    s_li = []
    answer = []
    for i in range(len(s)-1):
        if s[i] == '}':
            s_li.append(li)
            li = []
            continue
        if s[i].isdigit():
            li.append(int(s[i]))

    s_li.sort(key=lambda x:len(x))
    for i in range(len(s_li)):
        for j in range(len(s_li[i])):
            if s_li[i][j] not in answer:
                answer.append(s_li[i][j])

    return answer

def solution2(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

print(solution2("{{20,111},{111}}"))